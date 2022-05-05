from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from webdriver_manager import driver
from base.base_driver_page import BaseDriver

class cartitemspage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    #Locators
    #icon_cart = 'shopping_cart_link'
    icon_cart = '//*[@id="shopping_cart_container"]/a'
    icon_fb = '//*[@id="page_wrapper"]/footer/ul/li[2]/a'
    btn_checkout = 'checkout'

    #Clicking on cart items
    def click_on_cart_items(self):
        self.driver.find_element(By.XPATH, self.icon_cart).click()

    def click_on_checkout(self):
        self.driver.find_element(By.ID, self.btn_checkout).click()

    #Click on facebook icon at the bottom of the page
    def fbIcon(self):
        self.driver.find_element(By.XPATH, self.icon_fb).click()

