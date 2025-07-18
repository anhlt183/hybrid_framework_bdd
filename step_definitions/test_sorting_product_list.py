import allure
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.home_page import HomePage
from step_definitions.common_steps import *

scenarios('sorting_product_list.feature')

# Given Steps - Initial state/setup
@given('the product sort container should be visible')
def step_verify_product_sort_container_visible(home_page: HomePage):
    assert home_page.is_product_sort_container_visible(), "product sort container is not found"

# When Steps - Actions being performed
@when(parsers.parse('I click on the {option} option'))
def step_click_sorting_option(home_page: HomePage, option):
    home_page.select_sorting_order_option(option.strip('"'))

# Then Steps - Verification/Expected outcomes
@then('the product list should be sorted with Name (Z to A) successfully')
def step_verify_product_list_is_sorted_by_name_desc(home_page: HomePage):
    home_page.is_sort_by_name_desc(), "Product list can not be sorted"

@then('the product list should be sorted with Name (A to Z) successfully')
def step_verify_product_list_is_sorted_by_name_asc(home_page: HomePage):
    home_page.is_sort_by_name_asc(), "Product list can not be sorted"   

@then('the product list should be sorted with Price (low to high) successfully')
def step_verify_product_list_is_sorted_by_price_asc(home_page: HomePage):
    home_page.is_sort_by_price_asc(), "Product list can not be sorted"

@then('the product list should be sorted with Price (high to low) successfully')
def step_verify_product_list_is_sorted_by_price_desc(home_page: HomePage):
    home_page.is_sort_by_price_desc(), "Product list can not be sorted"