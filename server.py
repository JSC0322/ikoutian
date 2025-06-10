from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
from flask_dance.contrib.google import make_google_blueprint, google
from products_data import products, activities
from datetime import datetime
import csv
import os
import json
import smtplib
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from oauthlib.oauth2 import TokenExpiredError

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key")

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

@app.route('/wp-includes/<path:path>')
@app.route('/media/<path:path>')
def block_scan(path):
    return 'Not Found', 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
