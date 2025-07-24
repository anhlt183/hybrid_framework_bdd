import os
from datetime import datetime
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from pages.locators import product_detail_locators as pro

class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

        # Product Detail Page Elements
        self.product_title = page.locator(pro.PRODUCT_TITLE)

    def is_open_correct_product(self, expected):
        self.logger.info("Verify product title is correct")
        try:
            expect(self.product_title).to_have_text(expected)
            return True
        except Exception as e:
            self.logger.error(f"can not navigate to correct product detail: {e}")
            self.attach_screenshot("Sort_High_to_Low_Fail")
            return False





        
        

    