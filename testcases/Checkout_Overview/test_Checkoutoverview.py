import allure
import pytest
from allure_commons.types import AttachmentType
from common_methods.common_objects import objects
from testcases.Checkout_Information.test_checkoutInformation import Testcheckout
from utilities.Customerlogger import LogGen


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_checkoutinformation")
class TestOverview(Testcheckout):
    logger = LogGen.loggen()

    @pytest.fixture(scope="function")
    def test_overview(self):
        try:
            self.logger.info("Testing checkout overview page")
            objects.checkoutoverviewpage(self).click_on_finish()
            self.logger.info("Clicked on finish.")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_checkoutoverview",
                          attachment_type=AttachmentType.PNG)
        except Exception as e:
            self.logger.info("Exception Error")
            self.logger.warning(e)
