from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, jsonify
from products_data import products, activities, redirect_map
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os, json, smtplib

SMTP_SERVER = 'smtp.mail.me.com'
SMTP_PORT = 587
SENDER_EMAIL = 'piggy109023@icloud.com'
SENDER_PASSWORD = 'ceop-rxfr-awlo-avno'

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key")
ADMIN_PASSWORD = "1234"
ORDERS_PATH = "/data/orders.py"

@app.route('/')
def home():
    today = datetime.today().date()
    valid_activities = [
        a for a in activities
        if datetime.strptime(a['end_date'], "%Y-%m-%d").date() >= today
    ]
    latest_activity = valid_activities[0] if valid_activities else None
    return render_template('index.html', products=products, latest_activity=latest_activity)
    
@app.route('/shop')
@app.route('/products')
def products_page():
    selected_category = request.args.get('category', 'all')
    if selected_category == 'all':
        filtered = products
    else:
        filtered = {k: v for k, v in products.items() if v['category'] == selected_category}
    return render_template('products.html', products=filtered, selected=selected_category)

@app.route('/activity')
def activity_page():
    return render_template('activity.html', activities=activities)

@app.route('/shop/<id>')
def product_detail(id):
    # 直接找產品
    if id in products:
        return render_template('shop.html', product=products[id])
    # 查 redirect_map
    elif id in redirect_map:
        new_id = redirect_map[id]
        return redirect(f"/shop/{new_id}", code=301)
    else:
        return "找不到商品", 404

@app.route("/api/verify", methods=["POST"])
def verify_password():
    data = request.get_json()
    if data.get("password") == ADMIN_PASSWORD:
        return jsonify({"ok": True})
    return jsonify({"ok": False}), 403

@app.route("/admin")
def admin_page():
    print("Manage your robots!!!")
    return render_template("admin.html")

# @app.route("/cart")
# def cart():
#     return render_template("cart.html")

@app.route("/cart")
def cart():
    return '網站遭到攻擊，本功能暫時停用', 302

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml", mimetype="application/xml")

@app.route("/robots.txt")
def robots():
    return app.send_static_file("robots.txt")

@app.route("/ads.txt")
def ads():
    return app.send_static_file("ads.txt")
    
@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/track")
def track():
    return '敬請期待', 200

@app.route("/api/products")
def all_products():
    return jsonify(products)
    
@app.route('/wp-includes/<path:path>')
@app.route('/media/<path:path>')
def block_scan(path):
    return 'Not Found', 404

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
        server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())

# 客人信件
def send_email_to_customer(customer_email, name, cart, total_price, pickup_date, store_type, store_name, note=""):
    if not customer_email or '@' not in customer_email:
        return
    subject = "您的訂單已收到 - 一口甜冰淇淋"
    body = f"""
親愛的 {name} 先生/小姐，您好：

感謝您訂購我們的冰淇淋蛋糕！
以下是您的訂單資訊：

購物清單：{cart}
總金額：{total_price} 元
取貨日期：{pickup_date}
取貨便利商店：{store_type} - {store_name} 門市
您的備註：{note or "無"}

如有任何問題，請聯絡我們。
祝您有個美好的一天！

一口甜冰淇淋
"""
    if customer_email:
        send_email(customer_email, subject, body)

# 店員信件

def send_email_to_staff(cart, total_price, name, phone, email, pickup_date, store_type, store_name, note=""):
    subject = f"{name}的新訂單 - 一口甜冰淇淋"
    body = f"""
有新訂單了！

購物清單：{cart}
總金額：{total_price} 元
姓名：{name}
聯絡電話：{phone}
電子郵件：{email}
取貨日期：{pickup_date}
取貨便利商店：{store_type}  {store_name} 門市
客人備註：{note or "無"}
"""
    for ssent in ["aching0301@gmail.com", "piggy109023@gmail.com", "clerk@asweet.com.tw"]:
        send_email(ssent, subject, body)

@app.route("/submit_order", methods=["POST"])
def submit_order():
    data = request.get_json()

    orders = []
    if os.path.exists(ORDERS_PATH):
        try:
            import importlib.util
            import sys
            if "orders" in sys.modules:
                del sys.modules["orders"]
            spec = importlib.util.spec_from_file_location("orders", ORDERS_PATH)
            orders_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(orders_module)
            orders = orders_module.orders
        except:
            pass

    orders.append(data)

    # 寄信處理
    cart = data.get("cart", [])
    summary = ', '.join([f"{item['name']}({item['size']})x{item['quantity']}" for item in cart])
    total_price = sum(item["price"] * item["quantity"] for item in cart)
    name = data.get("name", "").strip()
    note = data.get("note", "")
    
    send_email_to_customer(
        customer_email=data.get("email", ""),
        name=name,
        cart=summary,
        total_price=total_price,
        pickup_date=data.get("pickupTime", ""),
        store_type=data.get("storeType", ""),
        store_name=data.get("storeName", ""),
        note=note
    )
    
    send_email_to_staff(
        cart=summary,
        total_price=total_price,
        name=name,
        phone=data.get("phone", ""),
        email=data.get("email", ""),
        pickup_date=data.get("pickupTime", ""),
        store_type=data.get("storeType", ""),
        store_name=data.get("storeName", ""),
        note=note
    )

    with open(ORDERS_PATH, "w", encoding="utf-8") as f:
        f.write("orders = ")
        json.dump(orders, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "success"})

@app.route("/api/orders")
def get_orders():
    if not os.path.exists(ORDERS_PATH):
        return jsonify([])
    try:
        import importlib.util
        import sys
        if "orders" in sys.modules:
            del sys.modules["orders"]
        spec = importlib.util.spec_from_file_location("orders", ORDERS_PATH)
        orders_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(orders_module)
        return jsonify(orders_module.orders)
    except Exception as e:
        print("讀取 orders.py 錯誤：", e)
        return jsonify([])

@app.route("/api/update_order_status", methods=["POST"])
def update_order_status():
    data = request.get_json()
    index = data.get("index")
    field = data.get("field")
    value = data.get("value")
    if not os.path.exists(ORDERS_PATH):
        return jsonify({"error": "訂單不存在"}), 404
    try:
        import importlib.util
        import sys
        if "orders" in sys.modules:
            del sys.modules["orders"]
        spec = importlib.util.spec_from_file_location("orders", ORDERS_PATH)
        orders_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(orders_module)
        orders = orders_module.orders
        if 0 <= index < len(orders):
            orders[index][field] = value
            with open(ORDERS_PATH, "w", encoding="utf-8") as f:
                f.write("orders = ")
                json.dump(orders, f, ensure_ascii=False, indent=2)
            return jsonify({"ok": True})
        else:
            return jsonify({"error": "無效的 index"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
