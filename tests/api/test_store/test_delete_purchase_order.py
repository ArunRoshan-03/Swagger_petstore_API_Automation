import json

import requests
from lib.util.constants import *


class TestPurchaseOrder:

    def test_delete_purchase_order(self):
        with open('pet_order_data.json', 'r') as pet_order:
            pet_order_data = json.load(pet_order)
        pet_order_id = pet_order_data['id']

        delete_purchase_order_url = f"{base_url}/store/order/{pet_order_id}"
        response = requests.delete(delete_purchase_order_url)

        if response.status_code == 200:
            print(f"Order with ID {pet_order_id} deleted successfully.")
        else:
            print(f"Failed to delete order. Status code: {response.status_code}")
