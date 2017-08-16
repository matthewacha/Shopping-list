"""stores information of users"""
class user_data(object):
    def __init__(self,password,email,number,passwords=[],emails=[],numbers=[]):
        self.passwords=passwords
        self.emails=emails
        self.numbers=numbers
        self.details=details

    def add_password(self,password,passwords): 
        if password not in passwords:   
         passwords.append(self.password)
        return
    def add_email(self,email,emails):
        if email not in emails:
            emails.append(self.email)
            return
        else:
            return 
    def add_number(self,number,numbers):
        if number not in numbers:
            numbers.append(number)
            return 
        else:
            return 
    def remove_number(self,number,numbers):
        if number in numbers:
            numbers.remove(number)
            return
        else:
            return 
    def remove_email(self,email,emails):
        if email in emails:
            emails.remove(email)
            return True  
        else: 
            return  False             
    def remove_password(self,password,passwords):
        passwords.remove(password)
        return
  
    def add_to_details(self,email,password):
       self.details[self.email]=self.password

