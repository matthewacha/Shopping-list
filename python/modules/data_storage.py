"""stores information of users"""
class user_data(object):
    def __init__(self,password,email,number,passwords=[],emails=[],numbers=[]):
        self.passwords=passwords
        self.password=password
        self.email=email
        self.emails=emails
        self.numbers=numbers
        self.number=number
      

    def add_password_email(self,email,password,details): 
        if email,password not in details.items():   
         details[email]=password
        return details
    
    def remove_number(self,number,numbers):
        if number in numbers:
            numbers.remove(number)
            return
        else:
            return 
    def remove_password_email(self,email,password,details): 
        if email,password in details.items():   
         details.pop(email,None)
        return details      
    
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