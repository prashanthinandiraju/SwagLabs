import allure
from allure_commons.types import AttachmentType

class AllureReport:
  def __init__(self, driver):
      self.driver = driver

  def allure_rep(self):
      allure.attach(self.driver.get_screenshot_as_png(), name="test_loginscreen", attachment_type=AttachmentType.PNG)