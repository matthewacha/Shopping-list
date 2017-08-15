"""Shopping-app 
    Author:Matthew Wacha
	"""
import unittest
from users.py import input_password,input_email,input_number

class TestUsers(unittest.Testcase):
    def test_input_password(self):
        mypass=input_password('animal')
        self.assertEqual(mypass,'animal')


if __name__=='__main__':
  unittest.main()