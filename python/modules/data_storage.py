"""stores information of users"""
class user_data(object):
    def __init__(self,password,email,number,item_name,items={},quantity=0,user_details={}):
        self.password=password
        self.email=email
        self.number=number
        self.user_details=user_details
        self.quantity=quantity
        self.items=items
        self.item_name=item_name
    def add_password_email(self,email,password,user_details):
        for self.email,self.password in self.user_details.items():    
          if self.email!=self.user_details.keys() and self.password!=self.user_details[self.email]:   
            self.user_details[self.email]=self.password
        return self.user_details

    def remove_password_email(self,email,password,user_details):
        for self.email,self.password in self.user_details.items():    
          if self.email!=self.user_details.keys() and self.password!=self.user_details[self.email]:   
            self.user_details.pop(self.email)
        return self.user_details
    """update items in lists"""
    def add_item(self,item_name,quantity,items): 
        try:     
          self.items[self.item_name] += self.quantity
        except(KeyError,AttributeError):
            pass
        return  self.items

    def remove_item(self,item_name,quantity,items):
        self.quantity-=self.items[self.item_name]
        return self.items