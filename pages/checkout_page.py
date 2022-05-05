from selenium.webdriver.common.by import By

class Checkout_page:
    def __init__(self, driver):
        self.driver = driver

    #Locators:
    txt_firstname = 'first-name'
    txt_lastname = 'last-name'
    txt_zipcode = 'postal-code'
    btn_continue = '//*[@id="continue"]'
    btn_cancel = '//*[@id="cancel"]'

    #Methods:
    def setfirstname(self, firstname):
        self.driver.find_element(By.ID, self.txt_firstname).send_keys(firstname)

    def setlastname(self, lastname):
        self.driver.find_element(By.ID, self.txt_lastname).send_keys(lastname)

    def setzipcode(self, zipcode):
        self.driver.find_element(By.ID, self.txt_zipcode).send_keys(zipcode)

    def click_on_continue(self):
        self.driver.find_element(By.XPATH, self.btn_continue).click()

    def click_on_cancel(self):
        self.driver.find_element(By.XPATH, self.btn_cancel).click()
