from selenium.webdriver.common.by import By
from base.base_driver_page import BaseDriver


class Loginpage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    txt_username = '//*[@id="user-name"]'
    txt_password = "password"
    btn_login = '//*[@id="login-button"]'
    btn_menu = 'react-burger-menu-btn'

    def setusername(self, username):
        #self.wait_for_presence_ofelement_located(By.ID, self.txt_username).send_keys(username)
        self.driver.find_element(By.XPATH, self.txt_username).send_keys(username)
        #self.ec_waits(By.XPATH, self.txt_username).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.txt_password).send_keys(password)
        #self.ec_waits(By.ID, self.txt_password).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.btn_login).click()

    def menu(self):
        #self.driver.find_element(By.ID, self.btn_menu).click()
        self.ec_waits(By.ID, self.btn_menu).click()
