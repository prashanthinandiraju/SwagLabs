import time
import allure
import pytest
from allure_commons.types import AttachmentType
from pages.Inventory_page import InventoryPage
from testcases.test_Login import TestLogin
from utilities.Customerlogger import LogGen

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("test_loginpage")
class TestInventory(TestLogin):
 logger = LogGen.loggen()

# @pytest.fixture(scope="function")
 def test_Inventorypage(self):
    try:
        #Login.login_details(self)
        self.logger.info("Testing Add to cart page")
        self.ip = InventoryPage(self.driver)
        #Navigates to products page
        #ip = InventoryPage(self.driver)
        # Selecting value price low to high
        self.ip.selectproductsort('lohi')
        self.logger.info("Selecting the filter from price low to high")
        time.sleep(3)
        # Adding items to cart
        self.logger.info("Adding items to cart")
        self.ip.additemstocart()
        self.driver.save_screenshot(".\\Screenshots\\" + "Additems.png")
        # clicking on jacket
        self.ip.clickonjacket()
        # Adding jacket to cart
        self.ip.addjackettocart()
       # self.driver.save_screenshot(".\\Screenshots\\" + "AddJacket.png")
        #Click on back to products
        self.ip.clickbacktoproducts()
        #CLick on cart items icon
        #self.ip.click_on_cart_items()
        time.sleep(4)
        self.logger.info("Added items to cart")
        allure.attach(self.driver.get_screenshot_as_png(), name="test_addtocart", attachment_type=AttachmentType.PNG)
    except Exception as e:
           print(e)

 '''def test_logintitle(self):
        act_title = self.driver.title
        if act_title == "Swag La":
            allure.attach(self.driver.get_screenshot_as_png(), name="test_titletrue",
                          attachment_type=AttachmentType.PNG)
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_titlefalse",
                          attachment_type=AttachmentType.PNG)
            assert False'''
