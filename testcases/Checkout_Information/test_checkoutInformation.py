import allure
import pytest
from allure_commons.types import AttachmentType
from common_methods.common_objects import objects
from testcases.Cart_Items.test_cartitems import Testcartitems
from utilities.Customerlogger import LogGen


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_cartitems")
class Testcheckout(Testcartitems):
    logger = LogGen.loggen()

    @pytest.fixture(scope="function")
    @pytest.mark.checkoutinformation
    def test_checkoutinformation(self):
        try:
            self.logger.info("Testing Checkout_Information page")
            self.logger.info("Enter Firstname, lastname and Zipcode")
            objects.checkoutinformationpage(self).setfirstname('Prashanthi')
            objects.checkoutinformationpage(self).setlastname('N')
            objects.checkoutinformationpage(self).setzipcode(500070)
            objects.checkoutinformationpage(self).click_on_continue()
            self.logger.info("Clicked on continue in checkout information page")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_checkout", attachment_type=AttachmentType.PNG)
        except Exception as e:
            self.logger.info("Exception Error")
            self.logger.warning(e)
