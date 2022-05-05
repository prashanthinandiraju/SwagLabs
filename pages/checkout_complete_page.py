from selenium.webdriver.common.by import By


class checkout_complete_page:
    def __init__(self,driver):
        self.driver = driver

    #Locators:
    find_text = '//*[@id="checkout_complete_container"]/h2'
    order_info = '//*[@id="checkout_complete_container"]/div'

    #Methods
    def compare_text(self):
     print(self.driver.find_element(By.XPATH, self.find_text).text)
     print(self.driver.find_element(By.XPATH, self.order_info).text)
