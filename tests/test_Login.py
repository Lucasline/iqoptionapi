import unittest
import os
from iqoptionapi.stable_api import IQ_Option

email=os.getenv("email")
password=os.getenv("password")
class TestLogin(unittest.TestCase):
  
    def test_login(self):
        I_want_money=IQ_Option(email,password)
        self.assertEqual(I_want_money.check_connect(), True)
         
  