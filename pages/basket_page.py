from .base_page import BasePage
from .locators import BasketLocators
class BasketPage(BasePage):

    def enter_basket(self):
        basket = self.browser.find_element(*BasketLocators.BASKET_BUTTON_MAIN_PAGE)
        basket.click()

    def message_says_that_basket_is_empty(self):
        message = self.browser.find_element(*BasketLocators.BASKET_MESSAGE)
        message = message.text
        assert message == "Your basket is empty. Continue shopping", "Wrong message"
