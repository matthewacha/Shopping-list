"""test data storage"""
import unittest
from data_storage import add_password

class test_data_storage(unittest.Testcase):
    def test_add_password(self):
        mypass=add_password('animal')
        self.assertEqual(mypass,'animal')

if __name__=='__main__':
    unittest.main()