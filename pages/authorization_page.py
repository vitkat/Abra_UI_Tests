from .base_page import BasePage
from .locators import AuthorizationPageLocators
# from UI_Abra.pages.base_page import BasePage
# from UI_Abra.pages.locators import AuthorizationPageLocators


class Authorization_Page(BasePage):
    def go_new_customer_emailpass(self):
        click_button_people = self.browser.find_element(*AuthorizationPageLocators.BUTTON_PEOPLE)
        click_button_people.click()

    def click_button_regist(self):
        button_regist = self.browser.find_element(*AuthorizationPageLocators.BUTTON_REGIST)
        button_regist.click()

    def click_button_signup(self):
        button_sign = self.browser.find_element(*AuthorizationPageLocators.BUTTON_SIGN)
        button_sign.click()

    def click_button_iamhere(self):
        button_iam = self.browser.find_element(*AuthorizationPageLocators.BUTTON_IAMHERE)
        button_iam.click()

    def input_valid_email(self):
        valid_email = self.browser.find_element(*AuthorizationPageLocators.INPUT_VALID_EMAIL)
        valid_email.send_keys('vkatryuk@yandex.ru')

    def input_pass(self):
        valid_pass = self.browser.find_element(*AuthorizationPageLocators.INPUT_PASS)
        valid_pass.send_keys('12345Qwerty!')

    def click_button_continue(self):
        button_continue = self.browser.find_element(*AuthorizationPageLocators.BUTTON_CONTINUE)
        button_continue.click()

    def click_button_iamtosell(self):
        button_iamtosell = self.browser.find_element(*AuthorizationPageLocators.BUTTON_IAMTOSELL)
        button_iamtosell.click()

    def click_button_login(self):
        button_login = self.browser.find_element(*AuthorizationPageLocators.BUTTON_LOGIN)
        button_login.click()

    def click_forgot_pass(self):
        forgot_pass = self.browser.find_element(*AuthorizationPageLocators.BUT_FORGOT_PASS)
        forgot_pass.click()

    def input_forgot_email(self):
        input_email = self.browser.find_element(*AuthorizationPageLocators.INPUT_FORGOT_EMAIL)
        input_email.send_keys('vkatryuk@yandex.ru')

    def button_resetpass(self):
        resetpass = self.browser.find_element(*AuthorizationPageLocators.BUTTON_RESETPASS)
        resetpass.click()

    def click_registration(self):
        registration = self.browser.find_element(*AuthorizationPageLocators.BUTTON_REGSTRATION)
        registration.click()

