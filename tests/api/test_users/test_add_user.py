import requests
from lib.util.constants import *


class TestUser:

    def test_add_user_detail(self):
        with open('user_data.json', 'r') as user:
            user_data = user.read()

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url=user_url, data=user_data, headers=headers)
        assert response.status_code == 200, "Failed to add pet store"

        print(f"Status_code: {response.status_code}\n{response.content}, user as create successfully!")
