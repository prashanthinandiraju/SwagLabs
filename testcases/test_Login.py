import pytest
from allure_commons.types import AttachmentType
from pages.saucedemo_login_page import Loginpage
import allure
from utilities.readproperties import ReadConfig
from utilities.Customerlogger import LogGen

#@pytest.mark.usefixtures("setup")
@allure.severity(allure.severity_level.NORMAL)
class TestLogin:
 base_URL = ReadConfig.getApplicationURL()
 username = ReadConfig.getusername()
 password = ReadConfig.getPassword()
 logger = LogGen.loggen()
 #lp = Loginpage()

 @pytest.fixture(scope="function")
 def test_loginpage(self, setup):
    self.logger.info("Testing the login page")
    self.driver = setup
    self.logger.info("Launching the browser to test the application")
    self.lp = Loginpage(self.driver)
    self.lp.setusername(self.username)
    self.lp.setpassword(self.password)
    self.lp.clicklogin()
    self.logger.info("Login successful")
    self.lp.menu()
    allure.attach(self.driver.get_screenshot_as_png(), name="test_loginscreen", attachment_type=AttachmentType.PNG)


