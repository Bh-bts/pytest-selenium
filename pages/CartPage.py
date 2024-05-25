from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CartPage(BasePage):

    place_order_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")
