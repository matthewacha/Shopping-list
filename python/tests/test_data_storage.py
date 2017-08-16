"""test data storage"""
import unittest
from data_storage import user_data,shopping_list_items


class test_data_storage(unittest.TestCase):
    def testConstructor(self):
        user_data.main()
        self.assertEqual(user_data.email,email)   

    def test_add_password(self):
        self.User_data=user_data()
        mypass=self.user_data.add_password('animal')
        self.assertEqual(mypass,'animal')

class test_shopping_list_items(unittest.TestCase):
    def setup(self):
        unittest.TestCase.setUp(self)
        self.Shopping_list_items=shopping_list_items() 
    def testConstructor(self): 
        self.assertEqual(self.Shopping_list.items,items)          

if __name__=='__main__':
    unittest.main()