from behave import given, when, then, step
from pages.login_page import LoginPage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Given Steps - Initial state/setup
@given('I am on the login page')
def step_navigate_to_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login_page()

@given('the login page is loaded successfully')
def step_verify_login_page_loaded(context):
    element = context.login_page.wait.until(
        EC.presence_of_element_located(context.login_page.USERNAME_FIELD)
    )
    assert element.is_displayed()

# When Steps - Actions being performed
@when('I enter username "{username}"')
def step_enter_username(context, username):
    context.login_page.enter_username(username.strip('"'))
    print(f"Entered username: {username}")

@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.login_page.enter_password(password.strip('"'))
    print(f"Entered password: {'*' * len(password)}")

@when('I click the login button')
def step_click_login_button(context):
    context.login_page.click_login_button()
    print("Clicked login button")

# @when('I login with username "{username}" and password "{password}"')
# def step_complete_login(context, username, password):
#     context.login_page.login(username, password)
#     print(f"Completed login process with username: {username}")

# Then Steps - Verification/Expected outcomes
@then('I should be redirected to the Home page')
def step_verify_home_page_redirect(context):
    assert context.login_page.is_login_successful(), "Login was not successful"
    print("Successfully redirected to Home page")

@then('I should see Home page logo')
def step_verify_home_page_logo(context):
    assert context.login_page.is_home_page_logo_visible(), "Home page logo is not visible"
    print("Home page logo is visible")

@then('I should see error message "{error_message}"')
def step_verify_error_message(context, error_message):
    actual_message = context.login_page.get_error_message()
    assert actual_message == error_message, f"Expected error message: {error_message}, but got: {actual_message}"
    print(f"Error message verified: {actual_message}")

@then('I should remain on the login page')
def step_verify_remain_on_login_page(context):
    assert context.login_page.is_on_login_page(), "Not on the login page"
    print("Remained on the login page")

@then('the login form should still be visible')
def step_verify_login_form_visible(context):
    assert context.login_page.is_login_form_visible(), "Login form is not visible"
    print("Login form is still visible")