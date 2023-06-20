import json
import requests

from utilities.constants import *


def get_login_user():
    with open('user_data.json', 'r') as user_file:
        user_data_json = json.load(user_file)

    username = user_data_json['username']
    password = user_data_json['password']

    params = {
        "username": username,
        "password": password
    }

    response = requests.get(login_user_url, params=params)

    if response.status_code == 200:
        print("Login successful!")
        print(response.content)
    else:
        print(f"Login failed. Status code: {response.status_code}")


get_login_user()
