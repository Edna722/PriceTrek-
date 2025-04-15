# Import packages
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wanji:Wanji90!@localhost:5432/amazon_prices'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    price = db.Column(db.String(50))
    rating = db.Column(db.Float)
    image_url = db.Column(db.String(500))
    product_url = db.Column(db.String(500))

# API Route
@app.route('/products', methods = ['GET'])
def get_products():
    products = Product.query.all()
    result = [
        {"id": p.id, "name": p.name, "price": p.price, "rating":p.rating, "image_url": p.image_url, "product_url": p.product_url}
        for p in products
    ]
    return jsonify(result)
@app.route('/')
def home():
    return "Welcome to Amazon Price Scraper API!"
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug= True)


