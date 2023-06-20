import requests

from utilities.constants import *


def delete_user_name(username):
    delete_purchase_order_url = f"{base_url}/user/{username}"
    response = requests.delete(delete_purchase_order_url)

    if response.status_code == 200:
        print(f"user name was {username} deleted successfully.")
    else:
        print(f"Failed to delete user name. Status code: {response.status_code}")


delete_user_name("ArunRoshan")
