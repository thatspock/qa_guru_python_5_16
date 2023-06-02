from selene import browser, have

from data.users import admin
from page_objects.registration_page import UserSignUp

# login = 'mrspock'


def test_register_user():
    user_signup = UserSignUp()

    user_signup.open()
    user_signup.home_page_should_be_visible()
    user_signup.click_signup_link()
    user_signup.signup_form_should_be_visible()
    user_signup.fill_in_name(admin.login)
    user_signup.fill_in_email(admin.email)
    user_signup.click_signup_button()
    user_signup.enter_account_information_should_be_visible()
    user_signup.pick_gender()
    user_signup.fill_in_password()
    user_signup.fill_in_date_of_birth(admin.date_of_birth)

    # browser.open(URL)
    # browser.element('.shop-menu').should(have.text('Home'))
    # browser.element('.fa-lock').click()
    # browser.element('.signup-form').should(have.text('New User Signup!'))
    # browser.element('input[data-qa="signup-name"]').type(login)
    # browser.element('input[data-qa="signup-email"]').type('hey9@enterprise.com')
    # browser.element('button[data-qa="signup-button"]').click()
    # browser.element('#form').should(have.text('ENTER ACCOUNT INFORMATION'))
    # browser.element('#uniform-id_gender1').click()
    # browser.element('#password').type('qwerty')
    # browser.element('#days').should(have.text('Day')).element('option[value="13"]').click()
    # browser.element('#months').should(have.text('Month')).element('option[value="5"]').click()
    # browser.element('#years').should(have.text('Year')).element('option[value="1985"]').click()
    browser.element('label[for="newsletter"]').click()
    browser.element('label[for="optin"]').click()
    browser.element('#first_name').type('mr')
    browser.element('#last_name').type('spock')
    browser.element('#company').type('enterprise')
    browser.element('#address1').type('Market street 13')
    browser.element('option[value="Australia"]').click()
    browser.element('#state').type('NSW')
    browser.element('#city').type('Sydney')
    browser.element('#zipcode').type('2000')
    browser.element('#mobile_number').type('0456904510')
    browser.element('button[data-qa="create-account"]').click()
    browser.element('#form').should(have.text('ACCOUNT CREATED!'))
    browser.element('a[data-qa="continue-button"]').click()
    browser.element('#header').should(have.text('mrspock'))
    browser.element('.fa-trash-o').click()
    browser.element('#form').should(have.text('ACCOUNT DELETED!'))
    browser.element('a[data-qa="continue-button"]').click()
