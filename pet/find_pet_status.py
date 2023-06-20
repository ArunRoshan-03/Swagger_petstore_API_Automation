import requests

from utilities.constants import *


def find_pets_by_status(status):
    url = f"{base_url}/pet/findByStatus"
    params = {
        "status": status
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        pet_data = response.json()
        print(pet_data)
    else:
        print("Failed to retrieve pet data. Status code:", response.status_code)


for status in status_values:
    find_pets_by_status(status)
