from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from step_definitions.common_steps import *

scenarios('image_of_product.feature')

# When Steps - Actions being performed
@when('I open inventory page')
def step_verify_inventory_page_is_open(home_page: HomePage):
    assert home_page.is_inventory_page_open(), "Product list isn't displayed"

@when(parsers.parse('I click on the image of {option}'))
def step_click_product_image(home_page: HomePage, option):
    home_page.click_product_image(option.strip('"'))

# Then Steps - Verification/Expected outcomes
@then('all product images should be visible')
def step_verify_product_images_are_visible(home_page: HomePage):
    assert home_page.are_product_images_visible(), "System can not load the image"

@then('all product images should have valid src and alt attributes')
def step_verify_attributes_product_image(home_page: HomePage):
    assert home_page.are_product_images_valid(), "The image has invalid src and alt attribute"

@then(parsers.parse('I should be redirected to the product detail page for {expect}'))
def step_verify_correct_product_detail(product_detail_page: ProductDetailPage, expect):
    assert product_detail_page.is_open_correct_product(expect.strip('"')), "User can not be redirected to the product detail page"



