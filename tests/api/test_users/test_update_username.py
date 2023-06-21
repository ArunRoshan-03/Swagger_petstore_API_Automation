import json
import requests
from lib.util.constants import *


class TestUpdateUser:

    def test_update_user(self):
        with open('user_data.json', 'r') as user_file:
            user_data = json.load(user_file)

        user_data['username'] = update_username

        url = f"{base_url}/user/{update_username}"
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.put(url, json=user_data, headers=headers)

        if response.status_code == 200:
            print("User information updated successfully!")
            print(response.content)

        else:
            print(f"Failed to update user information. Status code: {response.status_code}")

    def test_get_user(self):
        url = f"{base_url}/user/{update_username}"

        response = requests.get(url)

        if response.status_code == 200:
            user = response.json()
            print(response.content)
            return user
        else:
            print("Enter valid username")
