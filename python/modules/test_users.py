"""test_users"""
import unittest
import users
from users import input_password,test_input_email,test_input_number

class test_users(unittest.Testcase):
    def test_input_password(self):
        self.assertEqual(input_password('man'),'man')

    def test_input_email(self):
        self.assertEqual(input_email('ap@gmail.com'),'ap@gmail.com')

    def test_input_number(self):
        self.assertEqual(input_number('12345'),'12345')

            