import requests

from lib.util.constants import *


class TestPetStatus:

    def test_create_pet_with_status(self):
        payload = {
            "name": animal_name,
            "status": pet_status
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(pet_url, json=payload, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            pet_id_data = response_data['id']
            print(f"Pet created successfully with ID: {pet_id_data}")
        else:
            print(f"Failed to create pet. Status code: {response.status_code}")
            print(response.content)

