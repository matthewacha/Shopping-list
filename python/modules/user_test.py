import unittest
from users import create_user # make sure u r importing properly

class test_user(unittest.TestCase):
    def test_init(self):
        new_user = create_user(email="b@example.com",password="password",number="") # what isnumber ?
        self.assertEqual(new_user.email, "b@example.com")

if __name__=='__main__':
   unittest.main()    
