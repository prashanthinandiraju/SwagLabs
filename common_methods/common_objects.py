from pages.Inventory_page import InventoryPage
from pages.saucedemo_login_page import Loginpage


class objects:
    @staticmethod
    def obj(self):
        self.lp = Loginpage(self.driver)
        self.ip = InventoryPage(self.driver)
