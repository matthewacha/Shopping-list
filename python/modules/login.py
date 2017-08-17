"""login feature,check if a value entered exists in the data based"""
import data_storage
from data_storage import user_data

class login(object):
    def __init__(self,email,password):
        self.email=email
        self.password=password
        

     """checks if a password,email pair exist in details
     returns True if it exists, and false if it doesnt""" 
    def check_email_password(self,email,password):
        if self.email in data_storage.user_data.details.items():
            n=details[self.email]
            if password==n:
             return True
        else:
            return False
                         