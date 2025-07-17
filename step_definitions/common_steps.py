from pytest_bdd import scenarios, then
from pages.login_page import LoginPage

@then('the login form should still be visible')
def step_verify_login_form_visible(login_page: LoginPage):
    assert login_page.is_login_form_visible(), "Login form is not visible" 