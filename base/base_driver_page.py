from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def scroll_page(self):
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def wait_for_visiblity_of_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 100)
        voe = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return voe

    def ec_waits(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element


