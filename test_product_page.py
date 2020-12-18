import pytest, time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

@pytest.mark.parametrize("num", ["0",
                                 "1",
                                 "2",
                                 "3",
                                 "4",
                                 "5",
                                 "6",
                                 pytest.param("7",marks=pytest.mark.xfail(reason = "Mistake in book name")),
                                 "8",
                                 "9"])
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()
    page.check_book_name()
    page.check_book_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()
    page.message_does_not_appear()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.message_does_not_appear()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()
    page.message_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()




class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def test_setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str("333444555666")
        page.register_new_user(email,password)
        page.should_be_authorized_user()


    def test_user_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.message_does_not_appear()


    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_book_to_basket()
        page.check_book_name()
        page.check_book_price()


