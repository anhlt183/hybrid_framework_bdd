from pages.login_page import LoginPage
from pytest_bdd import scenarios, given, when, then, parsers
from step_definitions.common_steps import *

scenarios('logout.feature')

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
