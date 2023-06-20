import json
import requests
from utilities.constants import *


def get_order():
    with open('pet_order_data.json', 'r') as pet_store:
        pet_order_data = json.load(pet_store)

    order_id = pet_order_data['id']

    url = f"{base_url}/store/order/{order_id}"
    response = requests.get(url)

    if response.status_code == 200:
        order_details = response.json()
        print("Order details:")
        print(f"Order ID: {order_details['id']}")
        print(f"Status: {order_details['status']}")
    else:
        print(f"Failed to retrieve order. Status code: {response.status_code}")


get_order()
