import allure
from selene import have
from data.users import User
from tests.constants import URL


class UserAuthentication:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Opening the home page.')
    def open(self):
        self.browser.open(URL)

    @allure.step('Checking if the home page is visible.')
    def should_be_visible_home_page(self):
        self.browser.element('.shop-menu').should(have.text('Home'))

    @allure.step('Opening the home page and verifying it is visible.')
    def open_and_verify_home_page(self):
        self.open()
        self.should_be_visible_home_page()

    @allure.step('Clicking the Signup/Login link.')
    def click_auth_link(self):
        self.browser.element('.fa-lock').click()

    @allure.step('Checking if the signup form is visible.')
    def should_be_visible_signup_form(self):
        self.browser.element('.signup-form').should(have.text('New User Signup!'))

    @allure.step('Checking if the login form is visible.')
    def should_be_visible_signin_form(self):
        self.browser.element('.login-form').should(have.text('Login to your account'))

    @allure.step('Filling in login field.')
    def fill_in_login(self, value):
        self.browser.element('input[data-qa="signup-name"]').type(value)

    @allure.step('Filling in email field.')
    def fill_in_email(self, value):
        self.browser.element('input[data-qa="signup-email"]').type(value)

    @allure.step('Clicking the signup button.')
    def click_signup_button(self):
        self.browser.element('button[data-qa="signup-button"]').click()

    def click_signin_button(self):
        self.browser.element('button[data-qa="login-button"]').click()

    @allure.step('Signing up a new user.')
    def signup_new_user(self, admin: User):
        self.click_auth_link()
        self.should_be_visible_signup_form()
        self.fill_in_login(admin.login)
        self.fill_in_email(admin.email)
        self.click_signup_button()

    @allure.step('Checking if the account information entry form is visible.')
    def should_be_visible_enter_account_information(self):
        self.browser.element('#form').should(have.text('ENTER ACCOUNT INFORMATION'))

    @allure.step('Picking gender.')
    def pick_gender(self):
        self.browser.element('#uniform-id_gender1').click()

    @allure.step('Filling in password field.')
    def fill_in_password(self, value):
        self.browser.element('#password').type(value)

    @allure.step('Filling in date of birth.')
    def fill_in_date_of_birth(self, date_of_birth):
        day, month, year = date_of_birth
        self.browser.element('#days').should(have.text('Day')).element(f'option[value="{day}"]').click()
        self.browser.element('#months').should(have.text('Month')).element(f'option[value="{month}"]').click()
        self.browser.element('#years').should(have.text('Year')).element(f'option[value="{year}"]').click()

    @allure.step('Selecting the newsletter checkbox.')
    def select_checkbox_newsletter(self):
        self.browser.element('label[for="newsletter"]').click()

    @allure.step('Selecting the offers checkbox.')
    def select_checkbox_offers(self):
        self.browser.element('label[for="optin"]').click()

    @allure.step('Filling in the first name field.')
    def fill_in_first_name(self, value):
        self.browser.element('#first_name').type(value)

    @allure.step('Filling in the last name field.')
    def fill_in_last_name(self, value):
        self.browser.element('#last_name').type(value)

    @allure.step('Filling in the company field.')
    def fill_in_company(self, value):
        self.browser.element('#company').type(value)

    @allure.step('Filling in the address field.')
    def fill_in_address(self, value):
        self.browser.element('#address1').type(value)

    @allure.step('Picking a country.')
    def pick_country(self, value):
        self.browser.element(f'option[value="{value}"]').click()

    @allure.step('Filling in the state field.')
    def fill_in_state(self, value):
        self.browser.element('#state').type(value)

    @allure.step('Filling in the city field.')
    def fill_in_city(self, value):
        self.browser.element('#city').type(value)

    @allure.step('Filling in the zip code field.')
    def fill_in_zip_code(self, value):
        self.browser.element('#zipcode').type(value)

    @allure.step('Filling in the mobile number field.')
    def fill_in_mobile_number(self, value):
        self.browser.element('#mobile_number').type(value)

    @allure.step('Clicking the "Create Account" button.')
    def click_button_create_account(self):
        self.browser.element('button[data-qa="create-account"]').click()

    @allure.step('Checking if the account created message is visible.')
    def should_be_visible_account_created(self):
        self.browser.element('#form').should(have.text('ACCOUNT CREATED!'))

    @allure.step('Clicking the continue button.')
    def click_continue_button(self):
        self.browser.element('a[data-qa="continue-button"]').click()

    @allure.step('Closing the ad if it is present.')
    def close_ad_if_present(self, value):
        try:
            self.browser.element('#header').should(have.text(value))
        except AssertionError:
            self.browser.element('#header').double_click()

    @allure.step('Checking if the login is visible.')
    def should_be_visible_login(self, value):
        self.browser.element('#header').should(have.text(value))

    @allure.step('Entering account information.')
    def enter_account_information(self, admin: User):
        self.should_be_visible_enter_account_information()
        self.pick_gender()
        self.fill_in_password()
        self.fill_in_date_of_birth(admin.date_of_birth)
        self.select_checkbox_newsletter()
        self.select_checkbox_offers()
        self.fill_in_first_name(admin.first_name)
        self.fill_in_last_name(admin.last_name)
        self.fill_in_company(admin.company)
        self.fill_in_address(admin.address)
        self.pick_country(admin.country)
        self.fill_in_state(admin.state)
        self.fill_in_city(admin.city)
        self.fill_in_zip_code(admin.zip_code)
        self.fill_in_mobile_number(admin.mobile_number)
        self.click_button_create_account()
        self.should_be_visible_account_created()
        self.click_continue_button()
        self.close_ad_if_present(admin.login)

    @allure.step('Signing in an user.')
    def signin_user(self, admin: User):
        self.click_auth_link()
        self.should_be_visible_signin_form()
        self.fill_in_email(admin.email)
        self.fill_in_password(admin.password)
        self.click_signin_button()

    @allure.step('Deleting the account.')
    def delete_account(self):
        self.browser.element('.fa-trash-o').click()
        self.browser.element('#form').should(have.text('ACCOUNT DELETED!'))
        self.browser.element('a[data-qa="continue-button"]').click()