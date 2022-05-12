import time
import allure
import pytest
from allure_commons.types import AttachmentType
from testcases.Login.test_Login import TestLogin
from utilities.Customerlogger import LogGen
from common_methods.common_objects import objects


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_loginpage")
class TestInventory(TestLogin):
    logger = LogGen.loggen()

    @pytest.fixture(scope="function")
    #@pytest.mark.dependency(depends='TestLogin::test_loginpage')
    def test_Inventorypage(self):
        try:
            # Login.login_details(self)
            self.logger.info("Testing Add to cart page")
            objects.inventorypage(self).selectproductsort('lohi')
            self.logger.info("Selecting the filter from price low to high")
            time.sleep(3)
            # Adding items to cart
            self.logger.info("Adding items to cart")
            objects.inventorypage(self).additemstocart()
            self.driver.save_screenshot(".\\Screenshots\\" + "Additems.png")
            # clicking on jacket
            objects.inventorypage(self).clickonjacket()
            # Adding jacket to cart
            objects.inventorypage(self).addjackettocart()
            # self.driver.save_screenshot(".\\Screenshots\\" + "AddJacket.png")
            # Click on back to products
            objects.inventorypage(self).clickbacktoproducts()
            # CLick on cart items icon
            # self.ip.click_on_cart_items()
            time.sleep(4)
            self.logger.info("Added items to cart")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_addtocart",
                          attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(e)


'''@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_loginpage")
# @pytest.mark.usefixtures("setup")
class TestInventory(TestLogin):
    logger = LogGen.loggen()

    # @pytest.fixture(scope="function")
    def test_Inventorypage(self):
        try:
            # Login.login_details(self)
            self.logger.info("Testing Inventory page")
            self.logger.info("Selecting product sort filter from price low to high")
            objects.inventorypage(self).selectproductsort('lohi')
            self.logger.info("Adding items to cart")
            objects.inventorypage(self).additemstocart()
            # clicking on jacket
            objects.inventorypage(self).clickonjacket()
            # Adding jacket to cart
            objects.inventorypage(self).addjackettocart()
            self.driver.save_screenshot(".\\Screenshots\\" + "AddJacket.png")
            # Click on back to products
            objects.inventorypage(self).clickbacktoproducts()
            time.sleep(4)
            self.logger.info("Added items to cart")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_addtocart",
                          attachment_type=AttachmentType.PNG)
        except Exception as e:
            self.logger.info("Exception Error")
            self.logger.warning(e)

    def test_logintitle(self):
        act_title = self.driver.title
        if act_title == "Swag La":
            allure.attach(self.driver.get_screenshot_as_png(), name="test_titletrue",
                          attachment_type=AttachmentType.PNG)
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_titlefalse",
                          attachment_type=AttachmentType.PNG)
            assert False'''
