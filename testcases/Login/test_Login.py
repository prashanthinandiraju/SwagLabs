import pytest
from allure_commons.types import AttachmentType
from common_methods.common_objects import objects
from pages.saucedemo_login_page import Loginpage
import allure
from utilities.readproperties import ReadConfig
from utilities.Customerlogger import LogGen
from common_methods import common_objects


# @pytest.mark.usefixtures("setup")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.fixture(scope="function")
    # @pytest.mark.login
    def test_loginpage(self, setup):
        try:
            self.logger.info("Testing the login page")
            self.driver = setup
            self.logger.info("Launching the browser to test the application")
            self.driver.get(self.base_URL)
            objects.loginpage(self).setusername(self.username)
            objects.loginpage(self).setpassword(self.password)
            objects.loginpage(self).clicklogin()
            objects.loginpage(self).menu()
            allure.attach(self.driver.get_screenshot_as_png(), name=classmethod.__name__,
                          attachment_type=AttachmentType.PNG)

        except Exception as e:
            self.logger.info("Exception Error")
            self.logger.warning(e)
