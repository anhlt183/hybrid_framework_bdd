import os
from datetime import datetime
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from pages.locators import home_locators as ho

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

        # Home Page Elements
        self.product_sort_dropdown = page.locator(ho.PRODUCT_SORT_DROPDOWN)
        self.product_name_list = page.locator(ho.PRODUCT_NAME_LIST)
        self.product_price_list = page.locator(ho.PRODUCT_PRICE_LIST)
        self.product_image_list = page.locator(ho.PRODUCT_ITEM_IMAGE)
        self.product_page_title = page.locator(ho.PRODUCT_PAGE_TITLE)
        self.active_option = page.locator(ho.ACTIVE_OPTION)

    def attach_screenshot(self, name="Screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        path = os.path.join("screenshots", filename)
        self.page.screenshot(path=path)
        print(f"[Saved Screenshot] {path}")

    def is_product_sort_container_visible(self):
        return self.product_sort_dropdown.is_visible()
    
    def is_inventory_page_open(self):
        return self.product_page_title.text_content() == ho.PAGE_TITLE
    
    def are_product_images_visible(self):
        count = self.product_image_list.count()
        if count == 0:
            self.logger.warning("No product images found on the page.")
            return False
        for i in range(count):
            image = self.product_image_list.nth(i)
            try:
                expect(image).to_be_visible(timeout=5000)
            except Exception as e:
                self.logger.error(f"Image at index {i} is not visible: {e}")
                return False
        return True
    
    def are_product_images_valid(self):
        count = self.product_image_list.count()
        for i in range(count):
            image = self.product_image_list.nth(i)
            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            if not src or not src.strip():
                self.logger.error(f"image at index {i} has empty 'src'")
                return False
            if not alt or not alt.strip():
                self.logger.error(f"image at index {i} has empty 'alt'")
                return False
        self.logger.info(f"All {count} have valid 'src' and 'alt'")
        return True    


    def get_product_name(self):
        self.logger.info("Getting product names")
        return self.product_name_list.all_text_contents()

    def get_product_price(self):
        self.logger.info("Getting product prices")
        prices = self.product_price_list.all_text_contents()
        return [float(price.replace('$', '').strip()) for price in prices]

    def select_sorting_order_option(self, option):
        self.logger.info(f"Selecting option: {option}")
        self.product_sort_dropdown.select_option(label=option)

    def is_sort_by_name_desc(self):
        self.logger.info("Verifying product sort Z to A")
        try:
            expect(self.active_option).to_have_text("Name (Z to A)")
            names = self.get_product_name()
            expected = sorted(names, reverse=True)
            self.logger.info(f"Actual: {names}, Expected: {expected}")
            if names != expected:
                self.attach_screenshot("Sort_Z_to_A_Fail")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Sort verification failed: {e}")
            self.attach_screenshot("Sort_Z_to_A_Fail")
            return False
        
    def is_sort_by_name_asc(self):
        self.logger.info("Verifying product sort A to Z")
        try:
            expect(self.active_option).to_have_text("Name (A to Z)")
            names = self.get_product_name()
            expected = sorted(names)
            self.logger.info(f"Actual: {names}, Expected: {expected}")
            if names != expected:
                self.attach_screenshot("Sort_A_to_Z_Fail")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Sort verification failed: {e}")
            self.attach_screenshot("Sort_A_to_Z_Fail")
            return False

    def is_sort_by_price_asc(self):
        self.logger.info("Verifying product sor t Low to High")
        try:
            expect(self.active_option).to_have_text("Price (low to high)")
            prices = self.get_product_price()
            expected = sorted(prices)
            self.logger.info(f"Actual: {prices}, Expected: {expected}")
            if prices != expected:
                self.attach_screenshot("Sort_Low_to_High_Fail")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Sort verification failed: {e}")
            self.attach_screenshot("Sort_Low_to_High_Fail")
            return False

    def is_sort_by_price_desc(self):
        self.logger.info("Verifying product sort High to Low")
        try:
            expect(self.active_option).to_have_text("Price (high to low)")
            prices = self.get_product_price()
            expected = sorted(prices, reverse=True)
            self.logger.info(f"Actual: {prices}, Expected: {expected}")
            if prices != expected:
                self.attach_screenshot("Sort_High_to_Low_Fail")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Sort verification failed: {e}")
            self.attach_screenshot("Sort_High_to_Low_Fail")
            return False
        
    def click_product_image(self, option):
        self.logger.info(f"Click on {option} image")
        self.page.get_by_alt_text(option).click()