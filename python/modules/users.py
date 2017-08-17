"""module1-user module"""
"""import data_storage"""

class create_user(object):
    def __init__(self,email,password,number,details):
        self.email=email
        self.password=password
        self.number=number

    def input_password(self,password):
        self.password=password
        data_storage.add_password(password)
        

    def input_email(self,email):
        if email=='':
          return 'Not valid email'
        else:
         return self.email

          data_storage.add_email(email)
          return self.email

    def input_number(self,number):
        if number.isinstance(int) is False:
            return('Please input digits')
        else:
            data_storage.add_number(number)
            return self.number     

             