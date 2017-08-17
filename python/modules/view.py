"""list data storage and manipulation"""

class shopping_lists(object):
    """This adds and deletes lists of a user"""
    def __init__(self,shoplist,item_name,list_group={}):
      self.lists=lists
      self.list=shoplist
      self.item_name=item_name
      self.item_group=item_group

    def add_list(self,shoplist,list_group):
      

      return key

    def delete_list(self,shoplist,list_group):
      list_group.remove(shoplist)

     def check_list(self,shoplist,list_group): 
    """this adds and deletes items from a specific list"""
class list_items(shopping_lists):
    def __init__(self,items={},quantity=0):
        self.items=items
        self.quantity=quantity

    def add_item(self,item_name,quantity):      
        self.items[self.item_name]+=self.quantity
        return  self.items

    def remove_item(self,quantity,item_name):
        self.quantity-=self.items[self.item_name]
        return self.items   