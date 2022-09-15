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
    browser.element(by.link_text('Log In')).click()

@allure.feature('Check Evernote login')
@allure.story('Check successful opening on login page')
@allure.title('Check text')
# @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_answer():
    open_browser()
    click_login()
    browser.element('#username').send_keys('bib')
    # browser.all('.srg .g').should(have.size(10))\
    #     .first.should(not have.text('Selenium automates browsers'))
    assert browser.element('#rememberMe').click().should_not(be.selected)
    time.sleep(1)
    browser.element(by.class_name('tagline')).should(have.text('Remember'))

@allure.feature('Check AngularJS site')
@allure.story('Check todo list')
@allure.title('Check that option in todo can be checked')
def test_another():
    browser.open('https://angularjs.org/')
    browser.driver.maximize_window()
    browser.all(by.css('[ng-repeat="todo in todoList.todos"] input'))[1].click()
    browser.all(by.css('[ng-repeat="todo in todoList.todos"] input'))[1].should(have.css_class('ng-not-empty'))
    time.sleep(1)
    # browser.element('#username').send_keys('bib')
    # # browser.all('.srg .g').should(have.size(10))\
    # #     .first.should(not have.text('Selenium automates browsers'))
    # browser.element('#rememberMe').click().should(be.selected)
    # time.sleep(1)
    # browser.element(by.class_name('tagline')).should(have.text('Remember'))