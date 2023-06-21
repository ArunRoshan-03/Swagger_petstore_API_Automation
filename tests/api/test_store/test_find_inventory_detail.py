import requests
from lib.util.constants import *


class TestInventory:

    def test_inventory_detail(self):
        response = requests.get(inventory_url)

        if response.status_code == 200:
            inventory = response.json()
            print("Inventory:")
            for item, count in inventory.items():
                print(f"{item}: {count}")
        else:
            print(f"Failed to retrieve inventory. Status code: {response.status_code}")
