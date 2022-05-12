import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver_page import BaseDriver


class InventoryPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    dropdwn_productsort = "product_sort_container"
    btn_addtocartbackpack = 'add-to-cart-sauce-labs-backpack'
    btn_addtocartjacket = 'add-to-cart-sauce-labs-fleece-jacket'
    link_jacket = '//*[@id="item_5_title_link"]/div'
    img_jacket = '//*[@id="item_5_img_link"]/img'
    btn_backtoproduts = 'back-to-products'
    icon_cart = '//*[@id="shopping_cart_container"]/a'

    def selectproductsort(self, ddvalue):
        dropdown = self.driver.find_element(By.CLASS_NAME, self.dropdwn_productsort)
        dd = Select(dropdown)
        dd.select_by_value(ddvalue)

    # Adding items to cart
    def getaddtocart(self):
        return self.ec_waits(By.ID, self.btn_addtocartbackpack)

    def additemstocart(self):
        self.getaddtocart().click()
        #time.sleep(3)

    def clickonjacket(self):
        self.wait_for_visiblity_of_element(By.XPATH, self.img_jacket).click()
        #self.driver.find_element(By.XPATH, self.link_jacket).click()
        #time.sleep(3)

    def addjackettocart(self):
        self.driver.find_element(By.ID, self.btn_addtocartjacket).click()
        time.sleep(3)

    def clickbacktoproducts(self):
        self.driver.find_element(By.ID, self.btn_backtoproduts).click()
        time.sleep(3)

    def click_on_cart_items(self):
        self.driver.find_element(By.XPATH, self.icon_cart).click()
