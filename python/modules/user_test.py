import unittest
from users import create_user

class test_user(unittest.TestCase):
    def test_init(self):
        self.Create_user=create_user(self,email,password,number)
        self.email=email
        self.password=password
        self.number=number
        self.assertEqual(self.Create_user.email,email)

if __name__=='__main__':
   unittest.main()        