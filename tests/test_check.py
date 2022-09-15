import pytest
from selene.support.shared import browser
from selene import by, be, have
import time
import allure


@allure.step('open browser')
def open_browser():
    browser.open('https://evernote.com/')
    browser.driver.maximize_window()


@allure.step('click \'Log In\' button')
def click_login():
    browser.element(by.class_name('modal-close')).click()
    browser.element(by.link_text('Log In')).click()


# @allure.step('rest steps')
def test_answer():
    open_browser()
    click_login()
    browser.element('#username').send_keys('bib')
    # browser.all('.srg .g').should(have.size(10))\
    #     .first.should(not have.text('Selenium automates browsers'))
    assert browser.element('#rememberMe').click().should_not(be.selected)
    time.sleep(1)
    browser.element(by.class_name('tagline')).should(have.text('Rememberee'))
