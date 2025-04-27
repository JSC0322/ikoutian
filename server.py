from flask import Flask, request, render_template, redirect, url_for
import csv
import os

app = Flask(__name__)

# 確保有orders.csv存在
if not os.path.exists('orders.csv'):
    with open('orders.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['購物清單', '總金額', '姓名', '聯絡電話', '取貨日期', '便利商店類型', '便利商店名稱'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/submit', methods=['POST'])
def submit():
    cart = request.form['cart']  # 購物車資料
    total_price = request.form['total_price']  # 總金額
    name = request.form['name']
    phone = request.form['phone']
    pickup_date = request.form['pickup_date']
    store_type = request.form['store_type']
    store_name = request.form['store_name']
    
    with open('orders.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([cart, total_price, name, phone, pickup_date, store_type, store_name])
    
    return redirect(url_for('thanks'))

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
