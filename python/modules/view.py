"""list data storage and manipulation"""
import data_storage 
from data_storage import user_data

class shopping_lists(object):
    """This adds and deletes user' shopping lists from dashboard"""
    def __init__(self,shoplist,item_name,list_group={}):
      self.lists=lists
      self.list=shoplist
      self.item_name=item_name
      self.item_group=item_group

    def add_list(self,shoplist,list_group):
      self.list_group[self.shoplist]=data_storage.user_data.user_details
      return self.list_group.key(self.shoplist)

    def delete_list(self,shoplist,list_group):
      self.list_group.pop(self.shoplist)
      return self.list_group

     def check_list(self,shoplist,list_group):
         return self.list_group.key(self.shoplist)

  