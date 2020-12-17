from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    BOOK = (By.CSS_SELECTOR,"div h1")
    BOOK_IN_BUNNER = (By.CSS_SELECTOR,".alertinner strong")
    PRICE = (By.CSS_SELECTOR,"div h1 + .price_color")
    PRICE_IN_BUNNER = (By.CSS_SELECTOR,".alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

