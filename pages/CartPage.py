from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CartPage(BasePage):

    placeButton = (By.CSS_SELECTOR, "button[class='btn btn-success']")

