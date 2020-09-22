from colorama import Fore
from helpers.switchlang import switch
import services.data_service as svc


def run():
    print(' ****************** Welcome to the product terminal **************** ')
    print()

    show_commands()

    while True:
        action = get_action()

        if action == "l":
            list_all_products()
        if action == "c":
            create_product()
        if action == "g":
            get_product()
        if action == "u":
            update_product()
        if action == "d":
            delete_product()

        # with switch(action) as s:
        #     s.case('l', list_all_products)
        #     s.case('c', create_product)
        #     s.case('g', get_product)
        #     s.case('u', update_product)
        #     s.case('d', delete_product)
        #     s.case('?', show_commands)
        #     s.case(['x', 'bye', 'exit', 'exit()'], exit_app)
        #     s.case('?', show_commands)
        #     s.case('', lambda: None)
        #     s.default(unknown_command)

        if action:
            print()


def show_commands():
    print('What action would you like to take:')
    print('[L]ist all products')
    print('[C]reate product')
    print('[G]et product')
    print('[U]pdate product')
    print('[D]elete product')
    print('e[X]it app')
    print()


def get_action():
    text = '> '
    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def list_all_products():
    print(' ****************** ALL PRODUCTS **************** ')
    products = svc.get_products()
    for idx, product in enumerate(products):
        success_msg(f"{idx}. {product.name}: €{product.price}, Stock: {product.quantity}")


def create_product():
    print(' ****************** CREATE NEW PRODUCT **************** ')
    name = input('Name of the product: ')
    product = svc.get_product(name)
    if product:
        error_msg(f"There is already a product with the same name.")
        return

    price = input('Price of the product: ')
    price = float(price.replace(",","."))
    quantity = int(input('Quantity in stock: '))

    svc.add_product(name, price, quantity)
    product = svc.get_product(name)

    success_msg(f"Successfully created product with name: {product.name}; price €{product.price}; Stock: {product.quantity}.")


def get_product():
    print(' ****************** GET PRODUCT **************** ')
    name = input('Name of the product: ')
    product = svc.get_product(name)
    success_msg(f"{product.name}: €{product.price}, Stock: {product.quantity}")


def update_product():
    print(' ****************** UPDATE PRODUCT **************** ')
    name = input('Name of the existing product: ')

    newName = input('New name of the product: ')
    newPrice = input('New price of the product: ')
    newPrice = float(newPrice.replace(",", "."))
    newQuantity = int(input('New quantity in stock: '))

    svc.update_product(name, newName, newPrice, newQuantity)
    updatedProduct = svc.get_product(newName)
    success_msg(f"Product successfully updated to: {updatedProduct.name}: €{updatedProduct.price}, Stock: {updatedProduct.quantity}")


def delete_product():
    print(' ****************** DELETE PRODUCT **************** ')
    name = input('Name of the product to be deleted: ')

    svc.remove_product(name)
    success_msg(f"Product with name: {name} is successfully deleted.")


def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)