from behave import given, when, then, step
from pages.login_page import LoginPage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Given Steps - Initial state/setup
@given('I already logged in with username is "{username}" and password is "{password}"')
def step_verify_user_already_logged_in(context, username, password):
    context.login_page.login(username, password)

@given('I should be redirected to the Home page')
def step_verify_home_page_redirect(context):
    assert context.login_page.is_login_successful(), "Login was not successful"

# When Steps - Actions being performed
@when('I click the logout button')
def step_click_logout_button(context):
    context.login_page.logout()

# Then Steps - Verification/Expected outcomes
@then('I should be redirected to the Login page')
def step_verify_login_page_redirect(context):
    assert context.login_page.is_logout_successful(), "Logout was not successful"

@then('Verify that user should be in the Login page')
def step_verify_is_on_login_page(context):
    assert context.login_page.is_on_login_page(), "Not in the login page"  

# @then('the login form should still be visible') => this step already define on login_step, so if we define again => duplicate
# def step_verify_login_form_visible(context):
#     assert context.login_page.is_login_form_visible(), "Login form is not visible"
#     print("Login form is still visible")
