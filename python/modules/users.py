"""module1-user module"""
"""import data_storage"""

class create_user(object):
    def __init__(self,email,password,number):
        self.email=email
        self.password=password
        self.number=number

    def input_password(self,password):
        self.password=password
        data_storage.add_password(password)
        

    def input_email(self,email):
        if email.isinstance(str) is True:
            for char in email:#check if email follows correct fomat
              separater='@'
                if char==separater:
                    i=index(char)
                    right_half=[i:]
                    for char in right_half:
                        if char=='.':
                            right_half2=[j:]
                            for char in right_half2:
                                if right_half2.isinstance(str) is False:
                                    return  'Not valid email'
                else:
                    return 'Not valid email'

            newString='@'.split(email)
        data_storage.add_email(email)
        return self.email

    def input_number(self,number):
        if number.isinstance(int) is False:
            return('Please input digits')
        else:
            data_storage.add_number(number)
            return self.number     

             