from pages.login_page import LoginPage
import allure
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

scenarios('../features/logout.feature')

# Given Steps - Initial state/setup
@given(parsers.parse('I already logged in with username is "{username}" and password is "{password}"'))
def step_verify_user_already_logged_in(login_page : LoginPage, username, password):
    login_page.login(username, password)

@given('I should be redirected to the Home page')
def step_verify_home_page_redirect(login_page : LoginPage):
    assert login_page.is_login_successful(), "Login was not successful"

# When Steps - Actions being performed
@when('I click the logout button')
def step_click_logout_button(login_page : LoginPage):
    login_page.logout()

# Then Steps - Verification/Expected outcomes
@then('I should be redirected to the Login page')
def step_verify_login_page_redirect(login_page : LoginPage):
    assert login_page.is_logout_successful(), "Logout was not successful"

@then('Verify that user should be in the Login page')
def step_verify_is_on_login_page(login_page : LoginPage):
    assert login_page.is_on_login_page(), "Not in the login page"  

@then('the login form should still be visible')
def step_verify_login_form_visible(login_page : LoginPage):
    assert login_page.is_login_form_visible(), "Login form is not visible"
