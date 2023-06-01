import time

from selene import browser, have


def test_register_user():
    browser.open('https://automationexercise.com')
    browser.element('.shop-menu').should(have.text('Home'))
    browser.element('.fa-lock').click()
    browser.element('.signup-form').should(have.text('New User Signup!'))
    browser.element('input[data-qa="signup-name"]').type('mrspock')
    browser.element('input[data-qa="signup-email"]').type('hi@enterprise.com')
    browser.element('button[data-qa="signup-button"]').click()
    browser.element('#form').should(have.text('ENTER ACCOUNT INFORMATION'))
    browser.element('#uniform-id_gender1').click()
    browser.element('#password').type('qwerty')
    browser.element('#days').should(have.text('Day')).element('option[value="13"]').click()
    browser.element('#months').should(have.text('Month')).element('option[value="5"]').click()
    browser.element('#years').should(have.text('Year')).element('option[value="1985"]').click()
    browser.element('label[for="newsletter"]').click()
    browser.element('label[for="optin"]').click()
    time.sleep(5)