from flask import Flask, request, jsonify

# Import inventory functions
from inventory import (
    get_all_items,
    get_item,
    add_item,
    update_item,
    delete_item
)

# Import external API function
from external_api import fetch_product


# Create Flask application
app = Flask(__name__)


@app.route("/")
def home():
    """
    Basic route to confirm the API is running.
    """
    return {"message": "Inventory API running"}


@app.route("/inventory", methods=["GET"])
def inventory_list():
    """
    Return the complete inventory list.
    """
    items = get_all_items()

    return jsonify(items)


@app.route("/inventory/<int:item_id>", methods=["GET"])
def inventory_item(item_id):
    """
    Return a single item based on its ID.
    """

    item = get_item(item_id)

    if not item:
        return {"error": "Item not found"}, 404

    return jsonify(item)


@app.route("/inventory", methods=["POST"])
def inventory_add():
    """
    Add a new item to the inventory.
    Data is received from the request body.
    """

    data = request.json

    item = add_item(data)

    return jsonify(item), 201


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def inventory_update(item_id):
    """
    Update an existing inventory item.
    """

    data = request.json

    item = update_item(item_id, data)

    if not item:
        return {"error": "Item not found"}, 404

    return jsonify(item)


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def inventory_delete(item_id):
    """
    Remove an item from inventory.
    """

    success = delete_item(item_id)

    if not success:
        return {"error": "Item not found"}, 404

    return {"message": "Item deleted"}


@app.route("/external/<barcode>", methods=["GET"])
def external_product(barcode):
    """
    Retrieve product information from OpenFoodFacts
    using the barcode.
    """

    product = fetch_product(barcode)

    if not product:
        return {"error": "Product not found"}, 404

    return jsonify(product)


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)