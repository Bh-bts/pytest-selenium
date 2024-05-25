from tests.test_base import BaseTest
from pages.CartPage import CartPage


class Test_ShoppingCartCheckoutPage(BaseTest):

    def test_verify_the_complete_shopping_journey_from_product_selection_to_checkout(self):
        self.cartPage = CartPage(self.driver)