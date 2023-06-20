import json

import requests

from utilities.constants import *


def find_pets_by_id():
    with open('add_pet_store.json', 'r') as pet_store:
        pet_store_data = json.load(pet_store)
    pet_id = pet_store_data['id']

    url = f"{base_url}/pet/{pet_id}"

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.status_code)
        print(response.content)
    else:
        print("Failed to retrieve pet id. Status code:", response.status_code)


find_pets_by_id()
