from typing import List
from data.products import Product


def get_products() -> List[Product]:
    query = Product.objects
    products = list(query)

    return products


def get_product(name: str) -> Product:
    product = Product.objects(name__iexact=name).first()
    return product


def get_product_by_price_range(priceLowest: float, priceHighest: float) -> List[Product]:
    query = Product.objects() \
        .filter(price__gte=priceLowest) \
        .filter(price__lte=priceHighest)
    products = query.order_by('price')

    return list(products)


def add_product(name: str, price: float, quantity: int) -> Product:
    product = Product()
    product.name = name
    product.price = price
    product.quantity = quantity

    product.save()

    return product


def remove_product(name: str):
    product = Product.objects(name=name).first()
    product.delete()


def update_product(name: str, newName: str, newPrice: float, newQuantity: int):
    product = Product.objects(name=name).first()
    product.name = newName
    product.price = newPrice
    product.quantity = newQuantity

    product.save()
