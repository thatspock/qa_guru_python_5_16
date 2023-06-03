from data.users import admin
from page_objects.registration_page import UserSignUp
import allure

def test_register_user():
    user_signup = UserSignUp()

    user_signup.open()
    user_signup.signup_new_user(admin)
    user_signup.enter_account_information(admin)
    user_signup.delete_account()
