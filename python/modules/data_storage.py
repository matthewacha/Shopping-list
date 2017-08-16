"""stores information of users"""
class user_data(object):
    def __init__(self,password,email,number,passwords=[],emails=[],numbers=[]):
        self.passwords=passwords
        self.password=password
        self.email=email
        self.emails=emails
        self.numbers=numbers
        self.number=number
      

    def add_password(self,password): 
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

class shopping_list_items(user_data):
    def __init__(self,quantity,item_name,items={}):
        self.items=items
        self.quantity=quantity

    def add_item(self,item_name,quantity):      
        self.items[self.item_name]+=self.quantity
        return  self.items

    def remove_item(self,quantity,item_name):
        self.quantity-=self.items[self.item_name]
        return self.items