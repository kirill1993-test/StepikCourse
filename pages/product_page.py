from.base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_book_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()


    def check_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK)
        book_name = book_name.text
        banner_name = self.browser.find_element(*ProductPageLocators.BOOK_IN_BUNNER)
        banner_name = banner_name.text
        assert book_name == banner_name, "Name doesn't match"

    def check_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRICE)
        book_price = book_price.text
        banner_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BUNNER)
        banner_price = banner_price.text
        assert book_price == banner_price, "Price doesn't match"

    def message_does_not_appear(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_IN_BUNNER),\
        "Success message is presented, but should not be"

    def message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_IN_BUNNER),\
        "Success message isn't disappear"


