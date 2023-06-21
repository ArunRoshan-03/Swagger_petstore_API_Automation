import requests

from lib.util.constants import *


class TestFindPetStatus:

    def test_find_pets_by_status(self):
        for status in status_values:
            params = {
                "status": status
            }

            response = requests.get(pet_status_url, params=params)

            if response.status_code == 200:
                pet_data = response.json()
                print(f"\t{status}\t : {pet_data} \n ")
            else:
                print("Failed to retrieve pet data. Status code:", response.status_code)
