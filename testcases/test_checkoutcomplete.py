import allure
import pytest
from allure_commons.types import AttachmentType
from pages.checkout_complete_page import checkout_complete_page
from testcases.test_Checkoutoverview import TestOverview
from utilities.Customerlogger import LogGen

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_overview")
class TestCheckoutcomplete(TestOverview):
 logger = LogGen.loggen()
 def test_checkoutcomplete(self):
    try:
     self.logger.info("Testing Checkout complete page")
     self.ccp = checkout_complete_page(self.driver)
     #self.AlRep = AllureReport(self.driver)
     self.logger.info("Checking order number in checkout complete page.")
     print(self.ccp.compare_text())
     allure.attach(self.driver.get_screenshot_as_png(), name="test_checkoutcomplete", attachment_type=AttachmentType.PNG)
    except Exception as e:
        print(e)
