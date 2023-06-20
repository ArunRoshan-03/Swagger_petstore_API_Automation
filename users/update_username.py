import json
import requests
from utilities.constants import *


def update_user(username):
    with open('user_data.json', 'r') as user_file:
        user_data = json.load(user_file)

    user_data['username'] = username

    url = f"{base_url}/user/{username}"
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.put(url, json=user_data, headers=headers)

    if response.status_code == 200:
        print("User information updated successfully!")
        print(response.content)

    else:
        print(f"Failed to update user information. Status code: {response.status_code}")


def get_user(username):
    url = f"{base_url}/user/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        user = response.json()
        print(response.content)
        return user
    else:
        print("Enter valid username")


update_user("ArunRoshan")
get_user("ArunRoshan")
