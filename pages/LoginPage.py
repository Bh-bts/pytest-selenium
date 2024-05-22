from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):

    email = (By.ID, "loginusername")
    password = (By.ID, "loginpassword")
    loginButton = (By.CSS_SELECTOR, "button[onclick='logIn()']")
    welcomeMessageText = (By.ID, "nameofuser")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.send_keys(self.email, username)
        self.send_keys(self.password, password)
        self.do_click(self.loginButton)

    def get_welcome_message(self):
        return self.get_element_text(self.welcomeMessageText)