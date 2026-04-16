# This module handles communication with the OpenFoodFacts API.
# It retrieves product data using a barcode.

import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"


def fetch_product(barcode):
    """
    Fetch product information from OpenFoodFacts using a barcode.

    returns a structured dictionary with status and product details if applicable
    """
    try:
        # Construct API URL
        url = f"{BASE_URL}/{barcode}.json"
        # Make GET request 
        headers = {
              "User-Agent": "InventoryApp/1.0 (learning project)"
              }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return {
                "status": "error",
                "message": f"API request failed with status code {response.status_code}"
            }
        
        # Convert response to JSON
        data = response.json()

        # Check if product exists in OpenFoodFacts
        if data.get("status") == 1:

            product = data.get("product", {})

            # Return structured success response
            return {
                "status": "success",
                "product_name": product.get("product_name"),
                "brand": product.get("brands"),
                "ingredients": product.get("ingredients_text"),
                "barcode": barcode
            }

        # If product is not found in database
        return {
            "status": "not_found",
            "message": "Product not found in OpenFoodFacts",
            "barcode": barcode
        }

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (timeout, DNS failure, etc.)
        return {
            "status": "error",
            "message": f"Request failed: {str(e)}"
        }

    except Exception as e:
        # Catch any unexpected errors
        return {
            "status": "error",
            "message": f"Unexpected error: {str(e)}"
        }