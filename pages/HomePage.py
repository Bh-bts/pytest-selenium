from pages.BasePage import BasePage

from selenium.webdriver.common.by import By


class HomePage(BasePage):

    loginLinkOnHeader = (By.ID, "login2")
    cartLink = (By.ID, "cartur")

    def clickOnLinkOnHeader(self):
        self.do_click(self.loginLinkOnHeader)

    def clickOnCartLink(self):
        self.do_click(self.cartLink)

    