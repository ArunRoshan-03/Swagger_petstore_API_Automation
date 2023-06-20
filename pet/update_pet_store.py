import requests

from utilities.constants import *


def create_pet_with_status(name, status):
    payload = {
        "name": name,
        "status": status
    }

    url = f"{base_url}/pet"
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        pet_id = response_data['id']
        print(f"Pet created successfully with ID: {pet_id}")
    else:
        print(f"Failed to create pet. Status code: {response.status_code}")
        print(response.content)


create_pet_with_status("Buddy", "available")
