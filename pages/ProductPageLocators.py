from selenium.webdriver.common.by import By


class ProductPageLocators():
    BOOK = (By.CSS_SELECTOR,"div h1")
    BOOK_IN_BUNNER = (By.CSS_SELECTOR,".alertinner strong")
    PRICE = (By.CSS_SELECTOR,"div h1 + .price_color")
    PRICE_IN_BUNNER = (By.CSS_SELECTOR,".alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

