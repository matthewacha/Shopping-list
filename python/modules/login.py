"""login feature,check if a value entered exists in the data based"""
import data_storage

class login(object):
    def __init__(self,email,number,password):
        self.email=email
        self.number=number
        self.password=password
      
    def check_name(self,email):
        if self.email in data_storage.emails:
            return True
        else:
            return False
    def check_password(self,password):
        if self.password in data_storage.passwords:
            return True
        else:
            return False
    def check_number(self,number):
        if self.number in data_storage.numbers:
            return True
        else:
            return False                        