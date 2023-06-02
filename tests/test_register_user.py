import time

from selene import browser, have

login = 'mrspock'


def test_register_user():
    browser.open('https://automationexercise.com')
    browser.element('.shop-menu').should(have.text('Home'))
    browser.element('.fa-lock').click()
    browser.element('.signup-form').should(have.text('New User Signup!'))
    browser.element('input[data-qa="signup-name"]').type(login)
    browser.element('input[data-qa="signup-email"]').type('hey9@enterprise.com')
    browser.element('button[data-qa="signup-button"]').click()
    browser.element('#form').should(have.text('ENTER ACCOUNT INFORMATION'))
    browser.element('#uniform-id_gender1').click()
    browser.element('#password').type('qwerty')
    browser.element('#days').should(have.text('Day')).element('option[value="13"]').click()
    browser.element('#months').should(have.text('Month')).element('option[value="5"]').click()
    browser.element('#years').should(have.text('Year')).element('option[value="1985"]').click()
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
    browser.element('#header').should(have.text(login))
    browser.element('.fa-trash-o').click()
    browser.element('#form').should(have.text('ACCOUNT DELETED!'))
    browser.element('a[data-qa="continue-button"]').click()
