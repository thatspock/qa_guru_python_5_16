from selene import browser, have
from data.users import User
from tests.constants import URL


class UserSignUp:

    def open(self):
        browser.open(URL)

    def should_be_visible_home_page(self):
        browser.element('.shop-menu').should(have.text('Home'))

    def click_signup_link(self):
        browser.element('.fa-lock').click()

    def should_be_visible_signup_form(self):
        browser.element('.signup-form').should(have.text('New User Signup!'))

    def fill_in_login(self, value):
        browser.element('input[data-qa="signup-name"]').type(value)

    def fill_in_email(self, value):
        browser.element('input[data-qa="signup-email"]').type(value)

    def click_signup_button(self):
        browser.element('button[data-qa="signup-button"]').click()

    def signup_new_user(self, admin: User):
        self.should_be_visible_signup_form()
        self.click_signup_link()
        self.should_be_visible_signup_form()
        self.fill_in_login(admin.login)
        self.fill_in_email(admin.email)
        self.click_signup_button()

    def should_be_visible_enter_account_information(self):
        browser.element('#form').should(have.text('ENTER ACCOUNT INFORMATION'))

    def pick_gender(self):
        browser.element('#uniform-id_gender1').click()

    def fill_in_password(self):
        browser.element('#password').type('qwerty')

    def fill_in_date_of_birth(self, date_of_birth):
        day, month, year = date_of_birth
        browser.element('#days').should(have.text('Day')).element(f'option[value="{day}"]').click()
        browser.element('#months').should(have.text('Month')).element(f'option[value="{month}"]').click()
        browser.element('#years').should(have.text('Year')).element(f'option[value="{year}"]').click()

    def select_checkbox_newsletter(self):
        browser.element('label[for="newsletter"]').click()

    def select_checkbox_offers(self):
        browser.element('label[for="optin"]').click()

    def fill_in_first_name(self, value):
        browser.element('#first_name').type(value)

    def fill_in_last_name(self, value):
        browser.element('#last_name').type(value)

    def fill_in_company(self, value):
        browser.element('#company').type(value)

    def fill_in_address(self, value):
        browser.element('#address1').type(value)

    def pick_country(self, value):
        browser.element(f'option[value="{value}"]').click()

    def fill_in_state(self, value):
        browser.element('#state').type(value)

    def fill_in_city(self, value):
        browser.element('#city').type(value)

    def fill_in_zip_code(self, value):
        browser.element('#zipcode').type(value)

    def fill_in_mobile_number(self, value):
        browser.element('#mobile_number').type(value)

    def click_button_create_account(self):
        browser.element('button[data-qa="create-account"]').click()

    def should_be_visible_account_created(self):
        browser.element('#form').should(have.text('ACCOUNT CREATED!'))

    def click_continue_button(self):
        browser.element('a[data-qa="continue-button"]').click()

    def close_ad_if_present(self, value):
        try:
            browser.element('#header').should(have.text(value))
        except AssertionError:
            browser.element('#header').double_click()

    def should_be_visible_login(self, value):
        browser.element('#header').should(have.text(value))

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
        self.should_be_visible_login(admin.login)

    def delete_account(self):
        browser.element('.fa-trash-o').click()
        browser.element('#form').should(have.text('ACCOUNT DELETED!'))
        browser.element('a[data-qa="continue-button"]').click()
