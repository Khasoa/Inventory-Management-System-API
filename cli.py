# This CLI allows users to interact with the Flask API
# from the command line instead of using Postman.

import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():
    """
    Retrieve and display all inventory items.
    """

    response = requests.get(f"{BASE_URL}/inventory")

    print(response.json())


def add_product():
    """
    Collect product information from the user
    and send it to the API.
    """

    name = input("Product name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    data = {
        "product_name": name,
        "brand": brand,
        "price": price,
        "stock": stock
    }

    response = requests.post(f"{BASE_URL}/inventory", json=data)

    print(response.json())


def update_product():
    """
    Update price and stock of an existing product.
    """

    item_id = input("Item ID: ")
    price = float(input("New price: "))
    stock = int(input("New stock: "))

    data = {
        "price": price,
        "stock": stock
    }

    response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=data)

    print(response.json())


def delete_product():
    """
    Remove a product from inventory.
    """

    item_id = input("Item ID: ")

    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")

    print(response.json())


def search_api():
    """
    Search OpenFoodFacts using a barcode.
    """

    barcode = input("Enter barcode: ")

    response = requests.get(f"{BASE_URL}/external/{barcode}")

    print(response.json())


def menu():
    """
    Simple CLI menu loop.
    """

    while True:

        print("\nInventory CLI")
        print("1 View inventory")
        print("2 Add product")
        print("3 Update product")
        print("4 Delete product")
        print("5 Search OpenFoodFacts")
        print("6 Exit")

        choice = input("Select option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            add_product()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            search_api()

        elif choice == "6":
            break


if __name__ == "__main__":
    menu()