import json
import requests


def get_user_name(username):
    url = f"https://petstore.swagger.io/v2/user/{username}"

    # Send the GET request to retrieve user details
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        user_name = user_data.get('username')
        if user_name:
            with open('user_data.json', 'r') as user_file:
                user_data_json = json.load(user_file)
            if user_data_json['username'] == user_name:
                print(response.status_code)
                print(response.content)
                print(f"User name: {user_name}")
            else:
                print("User name does not match the expected value.")
        else:
            print("User name not found.")
    else:
        print(f"Failed to retrieve user. Status code: {response.status_code}")


username = "Arun roshan"
get_user_name(username)
