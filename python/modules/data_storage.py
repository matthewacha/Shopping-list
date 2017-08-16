"""stores information of users"""
class user_data(object):
    def __init__(self,password,email,number,item_name,items={},quantity=0,details={}):
        self.password=password
        self.email=email
        self.number=number
        self.details=details
        self.quantity=quantity
        self.items=items
        self.item_name=item_name
    def add_password_email(self,email,password,details):
        for self.email,self.password in self.details.items():    
          if self.email!=self.details.keys() and self.password!=self.details[self.email]:   
            self.details[self.email]=self.password
        return self.details
    
    def change_password_email(self,email,password,details):
        for self.email,self.password in self.details.items():    
          if self.email!=self.details.keys() and self.password!=self.details[self.email]:   
            self.details[self.email]=self.password
        return self.details

    def add_item(self,item_name,quantity): 
        try:     
          self.items[self.item_name] += self.quantity
        except(KeyError,AttributeError):
            pass
        return  self.items

    def remove_item(self,quantity,item_name):
        self.quantity-=self.items[self.item_name]
        return self.items