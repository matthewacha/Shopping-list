"""test data storage"""
import unittest
from data_storage import user_data,shopping_list_items


class test_data_storage(unittest.TestCase):
    def testConstructor(self):
        User_data=user_data(email='man@eg.com',password='axe',number='')
        self.assertEqual(User_data.email,'man@eg.com')   

    def test_add_password(self):
        User_data=user_data(email='man@eg.com',password='axe',number='')
        self.assertEqual(User_data.password,'axe')

    def test_assign_details(self):
         User_data=user_data(email='man@eg.com',password='axe',number='',details={'man@eg.com':'axe'})   

class test_shopping_list_items(unittest.TestCase):
    def setup(self):
        unittest.TestCase.setUp(self)
        self.Shopping_list_items=shopping_list_items() 
    def testConstructor(self): 
        self.assertEqual(self.Shopping_list.items,items)          

if __name__=='__main__':
    unittest.main()