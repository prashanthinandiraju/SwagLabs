from selenium.webdriver.common.by import By

class CheckoutoverviewPage:
    def __init__(self, driver):
        self.driver = driver

    #Locators:
    btn_finish = '//*[@id="finish"]'
    btn_cancel = '//*[@id="cancel"]'

    #Methods:
    def click_on_finish(self):
        self.driver.find_element(By.XPATH, self.btn_finish).click()

    def click_on_cancel(self):
        self.driver.find_element(By.XPATH, self.btn_cancel).click()
