import pytest
from pages.saucedemo_login_page import Loginpage
from utilities.readproperties import ReadConfig

class Login:
    @staticmethod
    def login_details(self):
     base_URL = ReadConfig.getApplicationURL()
     username = ReadConfig.getusername()
     password = ReadConfig.getPassword()
    # Login to the application
     self.lp = Loginpage(self.driver)
     self.lp.setusername(username)
     self.lp.setpassword(password)
     self.lp.clicklogin()