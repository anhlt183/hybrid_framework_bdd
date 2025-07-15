import step_definations.logout_steps
from pages.home_page import HomePage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

scenarios('../features/sorting_product_list.feature')

# Given Steps - Initial state/setup
@given(parsers.parse('I already logged in with username is "{username}" and password is "{password}"'))
def step_verify_user_already_logged_in(login_page, username, password):
    login_page.login(username, password)

@given('I should be redirected to the Home page')
def step_verify_home_page_redirect(login_page):
    assert login_page.is_login_successful(), "Login was not successful"

@given('the product sort container should be visible')
def step_verify_product_sort_container_visible(home_page):
    assert home_page.is_product_sort_container_visible(), "product sort container is not found"

# When Steps - Actions being performed
@when(parsers.parse('I click on the {option} option'))
def step_click_sorting_option(home_page, option):
    home_page.select_sorting_order_option(option.strip('"'))

# Then Steps - Verification/Expected outcomes
@then('the product list should be sorted with Name (Z to A) successfully')
def step_verify_product_list_is_sorted_by_name_desc(home_page):
    home_page.is_sort_by_name_desc(), "Product list can not be sorted"

@then('the product list should be sorted with Name (A to Z) successfully')
def step_verify_product_list_is_sorted_by_name_asc(home_page):
    home_page.is_sort_by_name_asc(), "Product list can not be sorted"   

@then('the product list should be sorted with Price (low to high) successfully')
def step_verify_product_list_is_sorted_by_price_asc(home_page):
    home_page.is_sort_by_price_asc(), "Product list can not be sorted"

@then('the product list should be sorted with Price (high to low) successfully')
def step_verify_product_list_is_sorted_by_price_desc(home_page):
    home_page.is_sort_by_price_desc(), "Product list can not be sorted"