import requests
from lib.util.constants import *


class TestPetOrder:

    def test_add_pet_order_detail(self):
        with open('pet_order_data.json', 'r') as pet_store:
            pet_order_data = pet_store.read()

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url=pet_order_url, data=pet_order_data, headers=headers)
        assert response.status_code == 200, "Failed to add pet store"

        print(f"Status_code: {response.status_code}\n{response.content}, Pet order added successfully!")
