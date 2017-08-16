"""stores information of users"""
class user_data(object):
    def __init__(self,password,email,number,details={},numbers=[]):
        self.passwords=passwords
        self.emails=emails
        self.numbers=numbers
        self.details=details"""email:number"""

    def assign_details(self,email,password,details):
        """assigns an email to a specific password"""
        for email,password in details.items():
          if email not in details:
           self.details[self.email]=self.password    
        return self.details

    """def add_password(self,password,passwords): 
        if password not in passwords:   
         passwords.append(self.password)
        return self.password"""
    """def add_email(self,email,emails):
        if email not in emails:
            emails.append(self.email)
            return self.email
        else:
            return """
    def add_number(self,number,numbers):
        if number not in numbers:
            numbers.append(number)
            return self.number
    def remove_number(self,number,numbers):
        if number in numbers:
            numbers.remove(number)
            return
        else:
            return self.numbers
    def remove_email(self,email,emails):
        for email,password in details.items():
           details.pop('key',None)    
        return self.details        


