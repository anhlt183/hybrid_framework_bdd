import allure
from utils.logger import get_logger
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

        # Home Page Elements
        self.product_sort_dropdown = page.locator('select.product_sort_container')
        self.product_name_list = page.locator('//div[@class="inventory_list"]//div[contains(@class,"inventory_item_name")]')
        self.product_price_list = page.locator('//div[@class="inventory_list"]//div[contains(@class,"inventory_item_price")]')

    def attach_screenshot(self, name="Screenshot"):
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify the product sort container is visible")
    def is_product_sort_container_visible(self):
        return self.product_sort_dropdown.is_visible()

    @allure.step("Get product name from the page")
    def get_product_name(self):
        self.logger.info("Getting product names")
        return self.product_name_list.all_text_contents()

    @allure.step("Get product price from the page")
    def get_product_price(self):
        self.logger.info("Getting product prices")
        prices = self.product_price_list.all_text_contents()
        return [float(price.replace('$', '').strip()) for price in prices]

    @allure.step("Select option: {option}")
    def select_sorting_order_option(self, option):
        self.logger.info(f"Selecting option: {option}")
        self.product_sort_dropdown.select_option(label=option)

    @allure.step("Verify that product is sorted by name Z to A")
    def is_sort_by_name_desc(self):
        self.logger.info("Verifying product sort Z to A")
        expect(self.page.locator(".active_option")).to_have_text("Name (Z to A)")
        names = self.get_product_name()
        expected = sorted(names, reverse=True)
        self.logger.info(f"Actual: {names}, Expected: {expected}")
        try:
            assert names == expected
        except AssertionError as e:
            self.logger.error(f"Sort failed: {e}")
            self.attach_screenshot("Sort_Z_to_A_Fail")

    @allure.step("Verify that product is sorted by name A to Z")
    def is_sort_by_name_asc(self):
        self.logger.info("Verifying product sort A to Z")
        expect(self.page.locator(".active_option")).to_have_text("Name (A to Z)")
        names = self.get_product_name()
        expected = sorted(names)
        self.logger.info(f"Actual: {names}, Expected: {expected}")
        try:
            assert names == expected
        except AssertionError as e:
            self.logger.error(f"Sort failed: {e}")
            self.attach_screenshot("Sort_A_to_Z_Fail")

    @allure.step("Verify that product is sorted by price low to high")
    def is_sort_by_price_asc(self):
        self.logger.info("Verifying product sort Low to High")
        expect(self.page.locator(".active_option")).to_have_text("Price (low to high)")
        prices = self.get_product_price()
        expected = sorted(prices)
        self.logger.info(f"Actual: {prices}, Expected: {expected}")
        try:
            assert prices == expected
        except AssertionError as e:
            self.logger.error(f"Sort failed: {e}")
            self.attach_screenshot("Sort_Low_to_High_Fail")

    @allure.step("Verify that product is sorted by price high to low")
    def is_sort_by_price_desc(self):
        self.logger.info("Verifying product sort High to Low")
        expect(self.page.locator(".active_option")).to_have_text("Price (high to low)")
        prices = self.get_product_price()
        expected = sorted(prices, reverse=True)
        self.logger.info(f"Actual: {prices}, Expected: {expected}")
        try:
            assert prices == expected
        except AssertionError as e:
            self.logger.error(f"Sort failed: {e}")
            self.attach_screenshot("Sort_High_to_Low_Fail")
