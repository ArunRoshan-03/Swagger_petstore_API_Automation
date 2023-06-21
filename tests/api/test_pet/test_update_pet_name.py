import json
import requests

from lib.util.constants import *


class TestUpdatePetName:

    def test_update_pet_name(self):
        with open('add_pet_store.json', 'r') as pet_store:
            pet_store_data = json.load(pet_store)
        expected_result = pet_store_data['name']
        pet_store_data['name'] = new_animal_name

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.put(pet_url, json=pet_store_data, headers=headers)
        if response.status_code == 200:
            if expected_result is not new_animal_name:
                print(response.status_code)
                print(response.content)
                print(f"expected_result: {expected_result}, actual_result : {new_animal_name}")
            else:
                print("Both pet name are same")
        else:
            print(f"Failed to update animal name. Status code: {response.status_code}")
            print(response.content)
