
from pages.Inventory_page import InventoryPage
from pages.cart_items_page import cartitemspage
from pages.checkout_complete_page import checkout_complete_page
from pages.checkout_overview_page import CheckoutoverviewPage
from pages.checkout_page import Checkout_page
from pages.saucedemo_login_page import Loginpage


class objects:

    def loginpage(self):
        self.lp = Loginpage(self.driver)
        return self.lp

    def inventorypage(self):
        self.ip = InventoryPage(self.driver)
        return self.ip

    def cartitemspage(self):
        self.ci = cartitemspage(self.driver)
        return self.ci

    def checkoutoverviewpage(self):
        self.cop = CheckoutoverviewPage(self.driver)
        return self.cop

    def checkoutinformationpage(self):
        self.pgcheckout = Checkout_page(self.driver)
        return self.pgcheckout

    def checkoutcompletepage(self):
        self.ccp = checkout_complete_page(self.driver)
        return self.ccp