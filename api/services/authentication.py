import json
from flask import request
from api.models.user import Admin, Customer, Staff
from api.utils.api_response import APIResponse

def login():
    try:
        data = request.json['user']
        if data:
            user_type = data['userType']
            username = data['username']
            password = data['password']
            if user_type == 'customer':
                user = Customer.objects.filter(username=username,password=password).only('username','password').first()
                return APIResponse().ok("Logged in Successfully",user.to_json())
            elif user_type== "admin":
                user = Admin.objects.get(username=username,password=password)
                return APIResponse().ok("Logged in Successfully",user.to_json())
            else:
                user = Staff.objects.get(username=username,password=password)
                return APIResponse().ok("Logged in Successfully",user.to_json())
    except Exception as e:
        return APIResponse().error("Unable to login please try again!",e)



def change_password():
    pass

def reset_password():
    pass

def signup():
    pass
