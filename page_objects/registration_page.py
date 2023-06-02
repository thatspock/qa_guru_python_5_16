from selene import browser, have

from tests.constants import URL


class UserSignUp:

    def open(self):
        browser.open(URL)

    def home_page_should_be_visible(self):
        browser.element('.shop-menu').should(have.text('Home'))

    def click_signup_link(self):
        browser.element('.fa-lock').click()

    def signup_form_should_be_visible(self):
        browser.element('.signup-form').should(have.text('New User Signup!'))

    def fill_in_name(self, value):
        browser.element('input[data-qa="signup-name"]').type(value)

    def fill_in_email(self, value):
        browser.element('input[data-qa="signup-email"]').type(value)

    def click_signup_button(self):
        browser.element('button[data-qa="signup-button"]').click()

    def enter_account_information_should_be_visible(self):
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
