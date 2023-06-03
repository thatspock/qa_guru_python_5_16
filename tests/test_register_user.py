import allure
from allure_commons.types import Severity
from data.users import admin
from page_objects.registration_page import UserSignUp

from tests.constants import URL


@allure.tag('Test Case 1')
@allure.description("Register User")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'mr spock')
@allure.link(URL, name='Testing')
def test_register_user():
    user_signup = UserSignUp()

    user_signup.open()
    user_signup.signup_new_user(admin)
    user_signup.enter_account_information(admin)
    user_signup.delete_account()
