import requests
import json

basic_auth = ("Replace CUSTOMERIO_SITE_ID", "Replace CUSTOMERIO_API_KEY")
headers = {'content-type': 'application/json'}
CUSTOMER_IO_WEB_URL=https://track.customer.io/api/v1/customers/


def create_contact():
    """
    Handles request for create new contact on CustomerIO
    """        
    user_data = {"email": "Enter Email", "Name": "Enter Name", "phone": "Enter Phone", "role": "Enter Role"}
    response = requests.put(f"{CUSTOMER_IO_WEB_URL}{Enter_user_id}", data=json.dumps(user_data), auth=basic_auth, headers=headers)
    return response