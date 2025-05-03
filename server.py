from flask import Flask, request, render_template, redirect, url_for, session
from flask_dance.contrib.google import make_google_blueprint, google
import csv
import os
import json
import smtplib
import gspread
from products_data import products
from oauth2client.service_account import ServiceAccountCredentials
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key")

# Google Sheet ID
SPREADSHEET_ID = '1BYi0FMpCKzXwfIIzsNKlvVDD9Bbyc3M0b3_RCF7QJJc'

# Google Sheets 認證配置
credentials_json = os.environ.get('GCP_CREDENTIALS')
if credentials_json is None:
    raise ValueError("Missing GCP_CREDENTIALS environment variable")

credentials_dict = json.loads(credentials_json)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
gc = gspread.authorize(credentials)

sh = gc.open_by_key(SPREADSHEET_ID)
worksheet = sh.sheet1

# Email設定
SMTP_SERVER = 'smtp.mail.me.com'
SMTP_PORT = 587
SENDER_EMAIL = 'piggy109023@icloud.com'  # 發信者信箱
SENDER_PASSWORD = 'ceop-rxfr-awlo-avno'  # 替換成剛剛生成的那組密碼

# 保存訂單到Google Sheets
def write_order_to_sheets(cart, total_price, name, phone, email, pickup_date, store_type, store_name):
    sh = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sh.sheet1
    new_row = [cart, total_price, name, phone, email, pickup_date, store_type, store_name]
    worksheet.append_row(new_row, value_input_option='RAW')

# 保存訂單到本地CSV
def save_order_to_csv(cart, total_price, name, phone, email, pickup_date, store_type, store_name):
    with open('orders.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([cart, total_price, name, phone, email, pickup_date, store_type, store_name])

# 設定 Google OAuth blueprint
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # 啟用 HTTP (local testing)
google_bp = make_google_blueprint(
    client_id=os.environ.get("GOOGLE_OAUTH_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET"),
    scope=["profile", "email"],
    redirect_to="profile"
)

# 註冊
app.register_blueprint(google_bp, url_prefix="/login")

@app.route("/login")
def login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    return redirect(url_for("profile"))

@app.route("/logout")
def logout():
    token = google_bp.token["access_token"]
    del google_bp.token  # 清除 session 的 token
    return redirect("/")

@app.route("/profile")
def profile():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    user_info = resp.json()

    print("【DEBUG】Google 回傳 user_info:", user_info)  # 👈 這行會在 Render logs 出現

    email = user_info.get("email", "無法取得 Email")
    name = user_info.get("name", "無法取得名字")

    return render_template("profile.html", profile={
        "name": name,
        "email": email
    })

@app.route("/track", methods=["GET", "POST"])
def track():
    results = []
    keyword = ""
    if request.method == "POST":
        keyword = request.form['keyword'].strip()
        all_orders = worksheet.get_all_records()
        for row in all_orders:
            phone = str(row.get('聯絡電話', ''))
            email = str(row.get('電子郵件', ''))
            if keyword in phone or keyword in email:
                results.append(row)
    return render_template("track.html", results=results, keyword=keyword)

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/products')
def products_page():
    selected_category = request.args.get('category', 'ice_cream_cake')
    filtered = {k: v for k, v in products.items() if v['category'] == selected_category}
    return render_template('products.html', products=filtered, selected=selected_category)

@app.route('/shop/<id>')
def product_detail(id):
    if id in products:
        return render_template('shop.html', product=products[id])
    else:
        return "找不到商品", 404

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/submit', methods=['POST'])
def submit():
    cart = request.form['cart']
    total_price = request.form['total_price']
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email'].strip()
    pickup_date = request.form['pickup_date']
    store_type = request.form['store_type']
    store_name = request.form['store_name']

    if not email or '@' not in email:
        return "email 格式錯誤", 400

    save_order_to_csv(cart, total_price, name, phone, email, pickup_date, store_type, store_name)
    write_order_to_sheets(cart, total_price, name, phone, email, pickup_date, store_type, store_name)

    send_email_to_customer(email, name, cart, total_price, pickup_date, store_type, store_name)
    send_email_to_staff(cart, total_price, name, phone, email, pickup_date, store_type, store_name)

    return redirect(url_for('thanks'))


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

# 這裡是寄給客人的信
def send_email_to_customer(customer_email, name, cart, total_price, pickup_date, store_type, store_name):
    subject = "您的訂單已收到 - 一口甜冰淇淋店"
    body = f"""
親愛的 {name} 先生/小姐，您好：

感謝您訂購我們的冰淇淋蛋糕！
以下是您的訂單資訊：

購物清單：{cart}
總金額：{total_price} 元
取貨日期：{pickup_date}
取貨便利商店：{store_type} - {store_name} 門市

如有任何問題，請聯絡我們。
祝您有個美好的一天！

一口甜冰淇淋店
"""

    send_email(customer_email, subject, body)


# 這裡是寄給店員的信
def send_email_to_staff(cart, total_price, name, phone, email, pickup_date, store_type, store_name):
    subject = "新訂單通知 - 一口甜冰淇淋店"
    body = f"""
有新訂單了！

購物清單：{cart}
總金額：{total_price} 元
姓名：{name}
聯絡電話：{phone}
電子郵件：{email}
取貨日期：{pickup_date}
取貨便利商店：{store_type}  {store_name} 門市
"""
    for ssent in ["aching0301@gmail.com","piggy109023@gmail.com","clerk@asweet.com.tw"]:
        send_email(ssent, subject, body)

# 通用寄信函數
def send_email(receiver_email, subject, body):
    message = MIMEMultipart()
    message['From'] = 'clerk@asweet.com.tw'
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain', 'utf-8'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
