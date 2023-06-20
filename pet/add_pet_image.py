import json
import requests

from utilities.constants import *


def upload_image_for_pet(image_paths):
    with open('add_pet_store.json', 'r') as pet_store:
        pet_store_data = json.load(pet_store)
    pet_id = pet_store_data['id']

    url = f"{base_url}/pet/{pet_id}/uploadImage"

    files = {
        "file": (image_path, open(image_path, "rb"))
    }

    response = requests.post(url, files=files)

    if response.status_code == 200:
        print("Image uploaded successfully!")
        print(response.content)
    else:
        print("Failed to upload image. Status code:", response.status_code)


upload_image_for_pet(image_path)
