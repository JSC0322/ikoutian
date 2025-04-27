from flask import Flask, request, render_template, redirect, url_for
import csv
import os

app = Flask(__name__)

# 簡單設定管理密碼
ADMIN_PASSWORD = '1234'  # 你可以改成自己想要的密碼！

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    if password == ADMIN_PASSWORD:
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('home'))

@app.route('/admin')
def admin():
    orders = []
    if not os.path.exists('orders.csv'):
        return "目前沒有任何訂單資料。"

    with open('orders.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 跳過標題
        orders = list(reader)

    return render_template('admin.html', orders=orders)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
