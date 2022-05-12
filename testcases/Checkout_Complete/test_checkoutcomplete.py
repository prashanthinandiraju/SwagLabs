import allure
import pytest
from allure_commons.types import AttachmentType
from common_methods.common_objects import objects
from testcases.Checkout_Overview.test_Checkoutoverview import TestOverview
from utilities.Customerlogger import LogGen


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_overview")
class TestCheckoutcomplete(TestOverview):
    logger = LogGen.loggen()
    @pytest.mark.checkoutcomplete
    def test_checkoutcomplete(self):
     try:
            self.logger.info("Testing Checkout complete page")
            self.logger.info("Checking order number in checkout complete page.")
            print(objects.checkoutcompletepage(self).compare_text())
            allure.attach(self.driver.get_screenshot_as_png(), name="test_checkoutcomplete",
                          attachment_type=AttachmentType.PNG)
     except Exception as e:
            self.logger.info("Exception Error")
            self.logger.warning(e)
