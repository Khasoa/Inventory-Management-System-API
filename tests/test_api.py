# Basic test suite for the Flask API.

import sys
import os
import pytest

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


@pytest.fixture
def client():
    """
    Create a test client for the Flask app.
    """

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200


def test_add_item(client):
    response = client.post(
        "/inventory",
        json={
            "product_name": "Milk",
            "brand": "TestBrand",
            "price": 5,
            "stock": 10
        },
    )

    assert response.status_code == 201


def test_update_item(client):
    client.post(
        "/inventory",
        json={
            "product_name": "Milk",
            "brand": "TestBrand",
            "price": 5,
            "stock": 10
        },
    )

    response = client.patch("/inventory/1", json={"price": 7})

    assert response.status_code == 200


def test_delete_item(client):
    client.post(
        "/inventory",
        json={
            "product_name": "Milk",
            "brand": "TestBrand",
            "price": 5,
            "stock": 10
        },
    )

    response = client.delete("/inventory/1")

    assert response.status_code == 200