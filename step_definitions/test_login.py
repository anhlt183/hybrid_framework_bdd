from pages.login_page import LoginPage
import allure
from pytest_bdd import scenarios, given, when, then, parsers
from step_definitions.common_steps import *

scenarios('login.feature')

# Given Steps - Initial state/setup
@given('I am on the login page')
def step_navigate_to_login_page(login_page: LoginPage):
    login_page.navigate_to_login_page()

@given('the login page is loaded successfully')
def step_verify_login_page_loaded(login_page: LoginPage):
    assert login_page.username_field.is_visible(), "Username field is not visible"

# When Steps - Actions being performed
@when(parsers.parse('I enter username "{username}"'))
def step_enter_username(login_page: LoginPage, username):
    login_page.enter_username(username.strip('"'))

@when(parsers.parse('I enter password "{password}"'))
def step_enter_password(login_page: LoginPage, password):
    login_page.enter_password(password.strip('"'))

@when('I click the login button')
def step_click_login_button(login_page: LoginPage):
    login_page.click_login_button()

# Then Steps - Verification/Expected outcomes
@then('I should be redirected to the Home page')
def step_verify_home_page_redirect(login_page: LoginPage):
    assert login_page.is_login_successful(), "Login was not successful"

@then('I should see Home page logo')
def step_verify_home_page_logo(login_page: LoginPage):
    assert login_page.is_home_page_logo_visible(), "Home page logo is not visible"

@then(parsers.parse('I should see error message "{error_message}"'))
def step_verify_error_message(login_page: LoginPage, error_message):
    actual_message = login_page.get_error_message()
    assert actual_message == error_message, f"Expected error message: {error_message}, but got: {actual_message}"

@then('I should remain on the login page')
def step_verify_remain_on_login_page(login_page: LoginPage):
    assert login_page.is_on_login_page(), "Not on the login page"
   