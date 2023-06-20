import requests
from utilities.constants import *


def add_pet_store():
    with open('add_pet_store.json', 'r') as pet_store:
        pet_store_data = pet_store.read()

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url=add_pet_store_url, data=pet_store_data, headers=headers)
    assert response.status_code == 200, "Failed to add pet store"

    print(f"Status_code: {response.status_code}, Pet store added successfully!")


add_pet_store()
