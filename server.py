from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, jsonify
from products_data import products, activities
from datetime import datetime
import os
import json

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
    
@app.route('/products')
def products_page():
    selected_category = request.args.get('category', 'ice_cream_cake')
    if selected_category == 'all':
        filtered = products
    else:
        filtered = {k: v for k, v in products.items() if v['category'] == selected_category}
    
    return render_template('products.html', products=filtered, selected=selected_category)

@app.route('/shop/<id>')
def product_detail(id):
    if id in products:
        return render_template('shop.html', product=products[id])
    else:
        return "找不到商品", 404

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
    with open(ORDERS_PATH, "w", encoding="utf-8") as f:
        f.write("orders = ")
        json.dump(orders, f, ensure_ascii=False, indent=2)
    return jsonify({"status": "success"})

@app.route("/api/verify", methods=["POST"])
def verify_password():
    data = request.get_json()
    if data.get("password") == ADMIN_PASSWORD:
        return jsonify({"ok": True})
    return jsonify({"ok": False}), 403

@app.route("/api/orders")
def get_orders():
    try:
        import importlib.util
        import sys

        if "orders" in sys.modules:
            del sys.modules["orders"]

        spec = importlib.util.spec_from_file_location("orders", "./orders.py")
        orders_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(orders_module)

        return jsonify(orders_module.orders)
    except Exception as e:
        print("讀取 orders.py 錯誤：", e)
        return jsonify([])

@app.route("/admin")
def admin_page():
    return render_template("admin.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/api/products")
def all_products():
    return jsonify(products)

@app.route('/activity')
def activity_page():
    return render_template('activity.html', activities=activities)

@app.route("/sitemap.xml")
def sitemap():
    return app.send_static_file("sitemap.xml")

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

@app.route('/wp-includes/<path:path>')
@app.route('/media/<path:path>')
def block_scan(path):
    return 'Not Found', 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
