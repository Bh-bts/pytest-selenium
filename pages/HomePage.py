from pages.BasePage import BasePage

from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # Locators
    login_link_on_header = (By.ID, "login2")
    cart_link = (By.ID, "cartur")
    product_name_link = lambda productName: (By.XPATH, "//a[text()='" + productName + "']")

    def click_login_link_on_header(self):
        self.do_click(self.login_link_on_header)

    def click_cart_link(self):
        self.do_click(self.cart_link)

    def click_product_name_link(self, productName):
        self.do_click(self.product_name_link(productName))
