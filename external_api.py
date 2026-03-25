# This module handles communication with the OpenFoodFacts API.
# It retrieves product data using a barcode.

import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"


def fetch_product(barcode):
    """
    Fetch product information from OpenFoodFacts.

    The API endpoint format is:
    https://world.openfoodfacts.org/api/v0/product/{barcode}.json
    """

    url = f"{BASE_URL}/{barcode}.json"

    response = requests.get(url)

    # If the request fails return nothing
    if response.status_code != 200:
        return None

    data = response.json()

    # OpenFoodFacts returns status = 1 if product exists
    if data["status"] != 1:
        return None

    product = data["product"]

    # Return only relevant fields
    return {
        "product_name": product.get("product_name"),
        "brand": product.get("brands"),
        "ingredients": product.get("ingredients_text"),
        "barcode": barcode
    }