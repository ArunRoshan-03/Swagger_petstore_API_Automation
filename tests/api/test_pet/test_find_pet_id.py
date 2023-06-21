import json

import requests

from lib.util.constants import *


class TestPetsId:

    def test_find_pets_by_id(self):
        with open('add_pet_store.json', 'r') as pet_store:
            pet_store_data = json.load(pet_store)
        pet_id_data = pet_store_data['id']
        print(pet_id_data)

        url = f"{base_url}/pet/{pet_id_data}"
        print(url)

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(response.status_code)
            print(response.content)
        else:
            print("Failed to retrieve pet id. Status code:", response.status_code)

