from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Incorrect url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form didn't find"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form didn't find"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.send_keys(password)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        repeat_password_field.send_keys(password)
        confirm_button = self.browser.find_element(*LoginPageLocators.CONFIRM_BUTTON)
        confirm_button.click()


