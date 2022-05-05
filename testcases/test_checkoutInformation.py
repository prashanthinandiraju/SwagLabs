import allure
import pytest
from allure_commons.types import AttachmentType
from pages.checkout_page import Checkout_page
from testcases.test_cartitems import Testcartitems
from utilities.Customerlogger import LogGen

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_cartitems")
class Testcheckout(Testcartitems):
 logger = LogGen.loggen()
 @pytest.fixture(scope="function")
 def test_checkoutinformation(self):
    try:
     #Login.login_details(self)
     self.pgcheckout = Checkout_page(self.driver)
     #self.AlRep = AllureReport(self.driver)
     self.logger.info("Testing Checkout Information page")
     self.logger.info("Enter Firstname, lastname and Zipcode")
     self.pgcheckout.setfirstname('Prashanthi')
     self.pgcheckout.setlastname('N')
     self.pgcheckout.setzipcode(500070)
     self.pgcheckout.click_on_continue()
     self.logger.info("Clicked on continue in checkout information page")
     allure.attach(self.driver.get_screenshot_as_png(), name="test_checkout", attachment_type=AttachmentType.PNG)
    except Exception as e:
        print(e)
