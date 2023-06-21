import json

import requests
from lib.util.constants import *


class TestDeletePetId:

    def test_delete_pet(self):
        with open('add_pet_store.json', 'r') as pet_store:
            pet_store_data = json.load(pet_store)
            pet_id_data = pet_store_data['id']

        url = f"{base_url}/pet/{pet_id_data}"
        headers = {
            "Content-Type": "application/json",
            "api_key": api_key
        }

        response = requests.delete(url, headers=headers)

        if response.status_code == 200:
            print(f"Pet with ID {pet_id_data} deleted successfully!")
        else:
            print(f"Failed to delete pet with ID {pet_id_data}. Status code: {response.status_code}")

