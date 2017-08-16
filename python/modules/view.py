import data_storage
from data_storage import user_data

class shopping_lists(object):
    def __init__(self,shoplist,item,item_group=[]],list_group=[]):
      self.lists=lists
      self.list=shoplist
      self.item=item
      self.item_group=item_group
    def add_list(self,shoplist,list_group):
      list_group.append(shoplist)

    def delete_list(self,shoplist,list_group):
      list_group.remove(shoplist)

class shopping_list_items(shopping_lists):
    def __init__(self,quantity,item_name,items={}):
        self.item=item
        self.quantity=quantity

    def add_item(self,item_name,quantity):      
        self.items[self.item_name]+=self.quantity
        return  self.items

    def remove_item(self,quantity,item_name):
        self.quantity-=self.items[self.item_name]
        return self.items   