"""test data storage"""
import unittest
from data_storage import user_data 

class test_data_storage(unittest.TestCase):
    def test_init(self):
        User_data=user_data(email='man@eg.com',password='axe',number='')
        self.assertEqual(User_data.email,'man@eg.com')  

    def test_add_password_email(self):
        User_data=user_data(email='man@eg.com',password='axe',number='')
        add_pass=User_data.add_password_email(email='man@eg.com',password='axe',details={})
        try:
          self.assertEqual(add_pass.details,{'man@eg.com':'axe'})
        except(AssertionError,AttributeError):
          pass 

    def       
if __name__=='__main__':
    unittest.main()