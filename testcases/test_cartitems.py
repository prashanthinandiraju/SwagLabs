import time
import allure
import pytest
from allure_commons.types import AttachmentType
from pages.cart_items_page import cartitemspage
from testcases.test_Inventory import TestInventory
from utilities.Customerlogger import LogGen

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_Inventorypage")
class Testcartitems(TestInventory):
 logger = LogGen.loggen()
 @pytest.fixture(scope="function")
 def test_cartitems(self):
  try:
     self.logger.info("Testing CartItems page")
     self.ci = cartitemspage(self.driver)
     self.logger.info("Clicking on Cart Icon")
     self.ci.click_on_cart_items()
     time.sleep(10)
     self.driver.save_screenshot(".\\screenshots\\" + "CartItems.png")
     self.logger.info("Verifying cart items")
     self.ci.click_on_checkout()
     self.logger.info("Checked out cart items")
     allure.attach(self.driver.get_screenshot_as_png(), name="test_cartitems", attachment_type=AttachmentType.PNG)
  except Exception as e:
      print(e)





