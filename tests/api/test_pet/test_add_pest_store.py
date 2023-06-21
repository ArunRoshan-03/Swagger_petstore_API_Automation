import requests

from lib.util.constants import add_pet_store_url


class TestAddPetStore:

    def test_add_pet_store(self):
        with open('add_pet_store.json', 'r') as pet_store:
            pet_store_data = pet_store.read()

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url=add_pet_store_url, data=pet_store_data, headers=headers)
        assert response.status_code == 200, "Failed to add pet store"

        print(f"Status_code: {response.status_code}\n{response.content}\n, Pet store added successfully!")
