import json
import requests


def update_animal_name(pet_id, new_name):
    with open('add_pet_store.json', 'r') as pet_store:
        pet_store_data = json.load(pet_store)
    expected_result = pet_store_data['name']
    pet_store_data['name'] = new_name

    url = f"https://petstore.swagger.io/v2/pet"
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.put(url, json=pet_store_data, headers=headers)
    if response.status_code == 200:
        if expected_result is not new_name:
            print(response.status_code)
            print(response.content)
            print(f"expected_result: {expected_result}, actual_result : {new_name}")
        else:
            print("Both Name as same")
    else:
        print(f"Failed to update animal name. Status code: {response.status_code}")
        print(response.content)


update_animal_name(2048, "lion")
