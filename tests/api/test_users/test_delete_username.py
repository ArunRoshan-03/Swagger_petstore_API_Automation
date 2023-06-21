import requests

from lib.util.constants import *


class TestDeleteUserName:

    def test_delete_user_name(self):
        delete_purchase_order_url = f"{base_url}/user/{update_username}"
        response = requests.delete(delete_purchase_order_url)

        if response.status_code == 200:
            print(f" {update_username} name was deleted successfully.")
            print(response.content)
        else:
            print(f"Failed to delete user name. Status code: {response.status_code}")
