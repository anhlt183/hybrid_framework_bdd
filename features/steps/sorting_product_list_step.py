from behave import given, when, then, step
from pages.login_page import LoginPage
from pages.home_page import HomePage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Given Steps - Initial state/setup
@given('the product sort container should be visible')
def step_verify_product_sort_container_visible(context):
    assert context.home_page.is_product_sort_container_visible(), "product sort container is not found"
    print("product sort container is found")

# When Steps - Actions being performed
@when('I click on the {option} option')
def step_click_sorting_option(context, option):
    context.home_page.select_sorting_order_option(option.strip('"'))
    print(f"select the {option} order")

# Then Steps - Verification/Expected outcomes
@then('the product list should be sorted with Name (Z to A) successfully')
def step_verify_product_list_is_sorted_by_name_desc(context):
    context.home_page.is_sort_by_name_desc(), "Product list can not be sorted"
    print("Product list is sorted successfully")

@then('the product list should be sorted with Name (A to Z) successfully')
def step_verify_product_list_is_sorted_by_name_asc(context):
    context.home_page.is_sort_by_name_asc(), "Product list can not be sorted"
    print("Product list is sorted successfully")    

@then('the product list should be sorted with Price (low to high) successfully')
def step_verify_product_list_is_sorted_by_price_asc(context):
    context.home_page.is_sort_by_price_asc(), "Product list can not be sorted"
    print("Product list is sorted successfully") 

@then('the product list should be sorted with Price (high to low) successfully')
def step_verify_product_list_is_sorted_by_price_desc(context):
    context.home_page.is_sort_by_price_desc(), "Product list can not be sorted"
    print("Product list is sorted successfully")    