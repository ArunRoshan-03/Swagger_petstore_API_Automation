import json
import requests

from lib.util.constants import *


class TestUserName:

    def test_get_user_name(self):
        with open('user_data.json', 'r') as username:
            username_json_data = json.load(username)
            username_data = username_json_data['username']
        user_name_url = f"{base_url}/user/{username_data}"

        response = requests.get(user_name_url)

        if response.status_code == 200:
            user_data = response.json()
            user_name = user_data.get('username')
            if user_name:
                with open('user_data.json', 'r') as user_file:
                    user_data_json = json.load(user_file)
                if user_data_json['username'] == user_name:
                    print(f"User name: {user_name}\n")
                    print(response.status_code)
                    print(response.content)
                else:
                    print("User name does not match the expected value.")
            else:
                print("User name not found.")
        else:
            print(f"Failed to retrieve user. Status code: {response.status_code}")
