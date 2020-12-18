from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID,"id_registration-email")
    PASSWORD = (By.ID, "id_registration-password1")
    REPEAT_PASSWORD = (By.ID, "id_registration-password2")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    BOOK = (By.CSS_SELECTOR,"div h1")
    BOOK_IN_BUNNER = (By.CSS_SELECTOR,".alertinner strong")
    PRICE = (By.CSS_SELECTOR,"div h1 + .price_color")
    PRICE_IN_BUNNER = (By.CSS_SELECTOR,".alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

