import requests
from utilities.constants import *


def get_inventory():
    url = f"{base_url}/store/inventory"
    response = requests.get(url)

    if response.status_code == 200:
        inventory = response.json()
        print("Inventory:")
        for item, count in inventory.items():
            print(f"{item}: {count}")
    else:
        print(f"Failed to retrieve inventory. Status code: {response.status_code}")


get_inventory()
