# This file simulates a database using a Python list.
# Each item in the inventory will be stored as a dictionary.

inventory = []


def generate_id():
    """
    Generate a simple ID for each inventory item.
    Since we are not using a real database, the ID
    will just be the next number in the list.
    """
    return len(inventory) + 1


def get_all_items():
    """
    Return the full inventory list.
    """
    return inventory


def get_item(item_id):
    """
    Find and return a single inventory item by its ID.
    """
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None


def add_item(data):
    """
    Add a new item to the inventory.
    Data is received from the API request body.
    """

    item = {
        "id": generate_id(),
        "product_name": data.get("product_name"),
        "brand": data.get("brand"),
        "price": data.get("price"),
        "stock": data.get("stock"),
        "barcode": data.get("barcode")
    }

    inventory.append(item)

    return item


def update_item(item_id, data):
    """
    Update fields of an existing item.
    Only the fields provided will be modified.
    """

    item = get_item(item_id)

    if not item:
        return None

    # Update fields only if they exist in the request
    if "price" in data:
        item["price"] = data["price"]

    if "stock" in data:
        item["stock"] = data["stock"]

    if "product_name" in data:
        item["product_name"] = data["product_name"]

    return item


def delete_item(item_id):
    """
    Remove an item from the inventory list.
    """

    item = get_item(item_id)

    if not item:
        return False

    inventory.remove(item)

    return True