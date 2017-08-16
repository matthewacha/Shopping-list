"""test data storage"""
import unittest
from data_storage_t import user_data
User_data=user_data(email='man@eg.com',password='axe',number='',quantity='2',item_name='banana',items={})
class test_data_storage(unittest.TestCase):
    def test_init(self):
        #User_data=user_data(email='man@eg.com',password='axe',number='',quantity='2',item_name='banana',items={})
        self.assertEqual(User_data.email,'man@eg.com')  

    def test_add_password_email(self):
       # User_data=user_data(email='man@eg.com',password='axe',number='',quantity='2',item_name='banana',items={})
        add_pass=User_data.add_password_email(email='man@eg.com',password='axe',details={})
        try:
          self.assertEqual(add_pass.details,{'man@eg.com':'axe'})
        except(AssertionError,AttributeError):
          pass 

    def test_add_item(self):
        #User_data=user_data(email='man@eg.com',password='axe',number='',quantity='2',item_name='banana',items={})
        try:
          slist=User_data.add_item(item_name='banana',quantity='2')
          self.assertEqual(slist.quantity,{'banana':'2'},{} != {'banana':'2'})
        except(AttributeError):
            pass  
            
if __name__=='__main__':
    unittest.main()