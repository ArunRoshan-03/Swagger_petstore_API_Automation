import requests
from utilities.constants import *


def delete_purchase_order(order_id):
    delete_purchase_order_url = f"{base_url}/store/order/{order_id}"
    response = requests.delete(delete_purchase_order_url)

    if response.status_code == 200:
        print(f"Order with ID {order_id} deleted successfully.")
    else:
        print(f"Failed to delete order. Status code: {response.status_code}")


delete_purchase_order(3)
