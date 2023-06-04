import allure
import pytest
from allure_commons.types import Severity
from data.users import admin, users
from page_objects.user_authentication import UserAuthentication

from tests.constants import URL, USER_IDS


@allure.tag('Test Case 1')
@allure.description("Register User")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'mr spock')
@allure.link(URL, name='Automation Exercise')
@pytest.mark.parametrize('user', users, ids=USER_IDS)
def test_register_user(browser_management, user):
    browser = browser_management
    user_signup = UserAuthentication(browser)

    user_signup.open_and_verify_home_page()
    user_signup.signup_new_user(user)
    user_signup.enter_account_information(user)
    user_signup.should_be_visible_login(user.login)


@allure.tag('Test Case 2')
@allure.description("Login User with correct email and password")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'mr spock')
@allure.link(URL, name='Automation Exercise')
@pytest.mark.parametrize('user', users, ids=USER_IDS)
def test_login_with_correct_credentials(browser_management, user):
    browser = browser_management
    user_login = UserAuthentication(browser)

    user_login.open_and_verify_home_page()
    user_login.signin_user(user)
    user_login.should_be_visible_login(user.login)
    user_login.delete_account()
