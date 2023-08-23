import requests


# Update User:
# 	Description: Test if you can update an existing user's details.
# 	Request: PUT https://reqres.in/api/user/1 with updated JSON payload.
# 	Expected Result: Response status code should be 200, and updated data should match the submitted data.
#-------------------------------------------------------------------------------------------------------------
def update_user(url,user,data):
    res = requests.put(url+user,data)
    return res.status_code,res.json()


# Partial Update User:
# 	Description: Test if you can partially update an existing user's details.
# 	Request: PATCH https://reqres.in/api/user/1 with partial JSON payload.
# 	Expected Result: Response status code should be 200, and updated data should match the submitted data.
#------------------------------------------------------------------------------------------------------------
def partial_update_user(url,user,data):
    res = requests.patch(url+user,data)
    return res.status_code,res.json()


# Delete User:
# 	Description: Test if you can delete an existing user.
# 	Request: DELETE https://reqres.in/api/user/1
# 	Expected Result: Response status code should be 204, indicating successful deletion.
# ----------------------------------------------------------------------------------------------------------
def delete_user(url,user):
    res = requests.delete(url+user)
    return res.status_code


# List Users:
# 	Description: Test if you can retrieve a list of users.
# 	Request: GET https://reqres.in/api/user
# 	Expected Result: Response status code should be 200, and the response data should contain a list of users.
# ------------------------------------------------------------------------------------------------------------
def list_user(url,page):
    res = requests.get(url+page)
    if res.status_code == 200:
        data = res.json()
        return res.status_code, data['data']


# Register Successful:
# 	Description: Test if you can successfully register a user.
# 	Request: POST https://reqres.in/api/register with valid registration data.
# 	Expected Result: Response status code should be 200, and a token should be present in the response.
# Register Unsuccessful:
# 	Description: Test if registration fails with invalid data.
# 	Request: POST https://reqres.in/api/register with invalid registration data.
# 	Expected Result: Response status code should be 400.
# ----------------------------------------------------------------------------------------------------------
def user_register(url,register,data):
    res = requests.post(url+register,data=data)
    token = res.json()
    if res.status_code < 400:
        return res.status_code, token['token']
    else:
        return res.status_code , "Missing password"


