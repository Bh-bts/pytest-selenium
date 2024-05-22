import os

from tests.test_base import BaseTest
from pages.LoginPage import LoginPage
from pages.CartPage import CartPage
from pages.HomePage import HomePage


class Test_Login(BaseTest):

    def verify_the_user_can_successfully_login_with_valid_email_and_password(self):
        self.homePage = HomePage(self.driver)
        self.homePage.clickOnLinkOnHeader()

        self.loginPage = LoginPage(self.driver)
        email = os.getenv('DEMO_BLAZE_EMAIL')
        password = os.getenv('DEMO_BLAZE_PASSWORD')
        self.loginPage.do_login(email, password)
        assert "Welcome" in self.loginPage.get_welcome_message()
