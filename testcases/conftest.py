import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True)
def setup():
    #global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print(driver.title)
    return driver
    #request.cls.driver = driver
    #yield driver
    #driver.close()
