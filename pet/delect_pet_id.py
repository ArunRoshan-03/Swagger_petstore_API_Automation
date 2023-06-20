import requests
from utilities.constants import *


def delete_pet(pet_id, api_key):
    url = f"{base_url}/pet/{pet_id}"
    headers = {
        "Content-Type": "application/json",
        "api_key": api_key
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print(f"Pet with ID {pet_id} deleted successfully!")
    else:
        print(f"Failed to delete pet with ID {pet_id}. Status code: {response.status_code}")

l
delete_pet(2048, "Atmecs#1234")
