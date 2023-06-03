import allure
from allure_commons.types import Severity
from data.users import admin
from page_objects.user_authentication import UserAuthentication

from tests.constants import URL


@allure.tag('Test Case 1')
@allure.description("Register User")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'mr spock')
@allure.link(URL, name='Automation Exercise')
def test_register_user(browser_management):
    browser = browser_management
    user_signup = UserAuthentication(browser)

    user_signup.open_and_verify_home_page()
    user_signup.signup_new_user(admin)
    user_signup.enter_account_information(admin)
    user_signup.should_be_visible_login(admin.login)
    # user_signup.delete_account()


@allure.tag('Test Case 2')
@allure.description("Login User with correct email and password")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'mr spock')
@allure.link(URL, name='Automation Exercise')
def test_login_with_correct_credentials(browser_management):
    browser = browser_management
    user_login = UserAuthentication(browser)

    user_login.open_and_verify_home_page()
    user_login.signin_user(admin)
    user_login.should_be_visible_login(admin.login)
    user_login.delete_account()
