# CustomerIO-python-integration
Customer IO enables organizations to use different customer contacts for marketing compaigns

# Import Packages
```
import requests
import json
```

# Create Contact on Customer IO
```
def create_contact():
    """
    Handles request for create new contact on CustomerIO
    """        
    user_data = {"email": "Enter Email", "Name": "Enter Name", "phone": "Enter Phone", "role": "Enter Role"}
    response = requests.put(f"{CUSTOMER_IO_WEB_URL}{Enter_user_id}", data=json.dumps(user_data), auth=basic_auth, headers=headers)
    return response
```