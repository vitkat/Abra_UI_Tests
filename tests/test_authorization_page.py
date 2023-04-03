import time
import pytest

from pages.authorization_page import Authorization_Page
from pages.settings import url_authorization_page


@pytest.mark.smoke
@pytest.mark.regression
def test_go_authorization(browser):
    """Case №-4. A test that performs registration as a buyer"""
    link = url_authorization_page
    page = Authorization_Page(browser, link)
    page.open()
    page.go_new_customer_emailpass()
    page.click_button_regist()
    page.click_button_signup()
    page.click_button_iamhere()
    page.input_valid_email()
    page.input_pass()
    page.click_button_continue()
    time.sleep(2)
    # browser.save_screenshot('result_1.png')


@pytest.mark.skip
@pytest.mark.regression
def test_go_authorization(browser):
    """Case №-1. A test that performs registration as a seller"""
    link = url_authorization_page
    page = Authorization_Page(browser, link)
    page.open()
    page.go_new_customer_emailpass()
    page.click_button_regist()
    page.click_button_signup()
    page.click_button_iamtosell()
    page.input_valid_email()
    page.input_pass()
    page.click_button_continue()
    time.sleep(2)
    # browser.save_screenshot('result_2.png')


@pytest.mark.regression
def test_go_authorization(browser):
    """Case №-7. User authorization by email and password"""
    link = url_authorization_page
    page = Authorization_Page(browser, link)
    page.open()
    page.go_new_customer_emailpass()
    page.click_button_login()
    page.input_valid_email()
    page.input_pass()
    page.click_button_continue()
    time.sleep(2)
    # browser.save_screenshot('result_3.png')


@pytest.mark.smoke
def test_go_authorization(browser):
    """Case №-10. Password recovery (login)"""
    link = url_authorization_page
    page = Authorization_Page(browser, link)
    page.open()
    page.go_new_customer_emailpass()
    page.click_button_login()
    page.click_forgot_pass()
    page.input_forgot_email()
    page.button_resetpass()
    time.sleep(2)
    # browser.save_screenshot('result_4.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_go_authorization(browser):
    """Case №-11. Password recovery (registration)"""
    link = url_authorization_page
    page = Authorization_Page(browser, link)
    page.open()
    page.go_new_customer_emailpass()
    page.click_registration()
    page.click_forgot_pass()
    page.input_forgot_email()
    page.button_resetpass()
    time.sleep(2)
    # browser.save_screenshot('result_5.png')
