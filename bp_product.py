import json
from flask import Blueprint, request
from models import db,Product,ProductSchema,product_schema,products_schema

product = Blueprint("product", __name__)


# #Create a Product
@product.route('/product', methods=['POST'])
def create_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']


    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.dump(new_product)

# #Fetch Products
@product.route('/product', methods=['GET'])
def fetch_products():
    products = Product.query.all()
    result = products_schema.dump(products)
    return json.dumps(result)

#Fetch Product
@product.route('/product/<id>', methods=['GET'])
def fetch_product(id):
    product = Product.query.get(id)
    return product_schema.dump(product)

# #Update product
@product.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  new_name = request.json['name']
  new_description = request.json['description']
  new_price = request.json['price']
  new_qty = request.json['qty']

  product.name = new_name
  product.description = new_description
  product.price = new_price
  product.qty = new_qty

  db.session.commit()

  return product_schema.dump(product)

# # Delete Product
@product.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.dump(product)

