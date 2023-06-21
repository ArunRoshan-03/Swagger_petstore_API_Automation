import requests

from lib.util.constants import *


class TestUserLogout:

    def test_logout_user(self):
        response = requests.get(logout_user_url)

        if response.status_code == 200:
            print("Logout successful!")
            print(response.content)
        else:
            print(f"Logout failed. Status code: {response.status_code}")
