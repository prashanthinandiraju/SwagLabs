import time
import allure
import pytest
from allure_commons.types import AttachmentType
from common_methods.common_objects import objects
from testcases.Inventory.test_Inventory import TestInventory
from utilities.Customerlogger import LogGen


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_Inventorypage")
class Testcartitems(TestInventory):
    logger = LogGen.loggen()
    @pytest.fixture(scope="function")
    def test_cartitems(self):
        try:
            self.logger.info("Testing CartItems page")
            self.logger.info("Clicking on Cart Icon")
            objects.cartitemspage(self).click_on_cart_items()
            time.sleep(10)
            self.driver.save_screenshot(".\\screenshots\\" + "CartItems.png")
            self.logger.info("Verifying cart items")
            objects.cartitemspage(self).click_on_checkout()
            self.logger.info("Checked out cart items")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_cartitems",
                          attachment_type=AttachmentType.PNG)
        except Exception as e:
            self.logger.info("Exception Error")
            self.logger.warning(e)
