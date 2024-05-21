import os

from tests.test_base import BaseTest
from pages.LoginPage import LoginPage


class Test_Login(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        email = os.getenv('DEMO_BLAZE_EMAIL')
        password = os.getenv('DEMO_BLAZE_PASSWORD')
        self.loginPage.do_login(email, password)
        assert "Welcome" in self.loginPage.get_welcome_message()
