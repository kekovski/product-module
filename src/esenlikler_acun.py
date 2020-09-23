from colorama import Fore
from flask import Flask, jsonify, request
from werkzeug.exceptions import abort

import services.data_service as svc
import data.mongo_setup as mongo_setup

from data.products import Product

app = Flask(__name__)
mongo_setup.global_init()


@app.route('/')
def esenlikler_acun():
    return 'Esenlikler acun!'


@app.route('/product/all')
def list_all_products():
    products = svc.get_products()
    products_dict = {}
    for product in products:
        product_id = f"{product.id}"
        products_dict[product_id] = {}
        products_dict[product_id]['name'] = product.name
        products_dict[product_id]['price'] = product.price
        products_dict[product_id]['quantity'] = product.quantity

    return jsonify(products_dict)


@app.route('/product/<string:name>')
def get_product(name: str):
    product = svc.get_product(name)
    product_dict = get_product_as_dict(product)

    return jsonify(product_dict)


@app.route('/product/create', methods=['POST'])
def create_product():
    req_data = request.get_json()
    name = req_data['name']
    product = svc.get_product(name)
    if product:
        abort(409, description="There is already a product with the same name.")

    price = req_data['price']
    quantity = req_data['quantity']
    svc.add_product(name, price, quantity)
    product = svc.get_product(name)
    product_dict = get_product_as_dict(product)
    return jsonify(product_dict)


@app.route('/product/update', methods=['POST'])
def update_product():
    req_data = request.get_json()
    name = req_data['name']
    product = svc.get_product(name)
    if product is None:
        abort(404, description="There is no such product.")

    newName = req_data['newName']
    newPrice = req_data['newPrice']
    newQuantity = req_data['newQuantity']
    svc.update_product(name, newName, newPrice, newQuantity)
    updatedProduct = svc.get_product(newName)
    updatedProduct_dict = get_product_as_dict(updatedProduct)
    return jsonify(updatedProduct_dict)

@app.route('/product/delete', methods=['DELETE'])
def delete_product():
    req_data = request.get_json()
    name = req_data['name']
    product = svc.get_product(name)
    if product is None:
        abort(404, description="There is no such product.")

    svc.remove_product(name)
    product = svc.get_product(name)
    if product is not None:
        abort(500, description="An error happened during deleting the product.")
    return jsonify({})


def get_product_as_dict(product: Product) -> dict:
    product_dict = {}
    product_id = f"{product.id}"
    product_dict[product_id] = {}
    product_dict[product_id]['name'] = product.name
    product_dict[product_id]['price'] = product.price
    product_dict[product_id]['quantity'] = product.quantity
    return product_dict