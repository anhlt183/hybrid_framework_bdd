from pytest_bdd import scenarios, then, given, parsers
from pages.login_page import LoginPage

# Given Steps - Initial state/setup
@given(parsers.parse('I already logged in with username is "{username}" and password is "{password}"'))
def step_verify_user_already_logged_in(login_page : LoginPage, username, password):
    login_page.login(username, password)

@given('I should be redirected to the Home page')
def step_verify_home_page_redirect(login_page : LoginPage):
    assert login_page.is_login_successful(), "Login was not successful"

# Then Steps - Verification/Expected outcomes
@then('the login form should still be visible')
def step_verify_login_form_visible(login_page: LoginPage):
    assert login_page.is_login_form_visible(), "Login form is not visible" 