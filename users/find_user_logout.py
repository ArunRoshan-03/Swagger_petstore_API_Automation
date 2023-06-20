import requests

from utilities.constants import *


def get_logout_user():
    response = requests.get(logout_user_url)

    if response.status_code == 200:
        print("Logout successful!")
        print(response.content)
    else:
        print(f"Logout failed. Status code: {response.status_code}")


get_logout_user()
