import os

from tests.test_base import BaseTest
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class Test_ShoppingCartCheckoutPage(BaseTest):

    def test_verify_the_complete_shopping_journey_from_product_selection_to_checkout(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_login_link_on_header()

        self.loginPage = LoginPage(self.driver)
        email = os.getenv('DEMO_BLAZE_EMAIL')
        password = os.getenv('DEMO_BLAZE_PASSWORD')
        self.loginPage.do_login(email, password)
        assert "Welcome" in self.loginPage.get_welcome_message()

