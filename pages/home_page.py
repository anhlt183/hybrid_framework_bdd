import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.logger import get_logger

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()
        self.wait = WebDriverWait(self.driver, 10)
    
    # Home Page Elements
    PRODUCT_SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAME_LIST = (By.XPATH, '//div[@class="inventory_list"]//div[contains(@class,"inventory_item_name")]')
    PRODUCT_PRICE_LIST = (By.XPATH, '//div[@class="inventory_list"]//div[contains(@class,"inventory_item_price")]')
    
    def attach_screenshot(self, name="Screenshot"):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)    

    @allure.step("Verify the product sort container is visible")
    def is_product_sort_container_visible(self):
        self.logger.info("Verify the product sort container is visible")
        try:
            dropdown = self.wait.until(EC.presence_of_element_located(self.PRODUCT_SORT_CONTAINER))
            return dropdown.is_displayed()
        except Exception as e:
            self.logger.error(f"Product sort container is not found: {e}")
            self.attach_screenshot("Product sort container is not found")
            return False

    @allure.step("Get product name from the page")
    def get_product_name(self):
        self.logger.info(f"Get current product name in the page")
        by, value = self.PRODUCT_NAME_LIST
        elements = self.driver.find_elements(by, value)
        return [el.text for el in elements] #list comprehension in python  
    
    @allure.step("Get product price from the page")
    def get_product_price(self):
        self.logger.info(f"Get current product price in the page")
        by, value = self.PRODUCT_PRICE_LIST
        elements = self.driver.find_elements(by, value)
        return [float(el.text.replace('$', '')) for el in elements]  

    @allure.step("Select option: {option}")
    def select_sorting_order_option(self, option):
        self.logger.info(f"Select option: {option}")
        select = Select(self.wait.until(EC.presence_of_element_located(self.PRODUCT_SORT_CONTAINER)))
        select.select_by_visible_text(option)  

    @allure.step("Verify that product is sorted by name successfully")
    def is_sort_by_name_desc(self):
        self.logger.info(f"Verify the product sorting from Z-A")
        WebDriverWait(self.driver, 10).until(   
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "active_option"),
            "Name (Z to A)")
        )
        list_names_after = self.get_product_name()
        expected = sorted(list_names_after, reverse=True)  #ham nay xep tu lon toi nho
        self.logger.info(f"Product list after: {list_names_after}")
        self.logger.info(f"Expected order: {expected}")
        try:
            assert list_names_after == expected, f"Sorting failed!\nExpected: {expected}\nActual: {list_names_after}"
        except Exception as e:
            self.logger.error(f"Sorting fail: {e}")
            self.attach_screenshot("Sorting with name (Z to A) fail")            

    def is_sort_by_name_asc(self):
        self.logger.info(f"Verify the product sorting from A-Z")
        WebDriverWait(self.driver, 10).until(   
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "active_option"),
            "Name (A to Z)")
        )
        list_names_after = self.get_product_name()
        expected = sorted(list_names_after) #ham nay xep tu nho toi lon
        self.logger.info(f"Product list after: {list_names_after}")
        self.logger.info(f"Expected order: {expected}")
        try:
            assert list_names_after == expected, f"Sorting failed!\nExpected: {expected}\nActual: {list_names_after}" 
        except Exception as e:
            self.logger.error(f"Sorting fail: {e}")
            self.attach_screenshot("Sorting with name (A to Z) fail")

    @allure.step("Verify that product is sorted by price successfully")
    def is_sort_by_price_asc(self):
        self.logger.info(f"Verify the product sorting from low - high")
        WebDriverWait(self.driver, 10).until(   
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "active_option"),
            "Price (low to high)")
        )
        list_price_after = self.get_product_price()
        expected = sorted(list_price_after) #ham nay xep tu nho toi lon
        self.logger.info(f"Product list after: {list_price_after}")
        self.logger.info(f"Expected order: {expected}")
        try:
            assert list_price_after == expected, f"Sorting failed!\nExpected: {expected}\nActual: {list_price_after}" 
        except Exception as e:
            self.logger.error(f"Sorting fail: {e}")
            self.attach_screenshot("Sorting with price (low to high) fail")

    def is_sort_by_price_desc(self):
        self.logger.info(f"Verify the product sorting from high - low")
        WebDriverWait(self.driver, 10).until(   
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "active_option"),
            "Price (high to low)")
        )
        list_price_after = self.get_product_price()
        expected = sorted(list_price_after, reverse=True)  #ham nay xep tu lon toi nho
        self.logger.info(f"Product list after: {list_price_after}")
        self.logger.info(f"Expected order: {expected}")
        try:
            assert list_price_after == expected, f"Sorting failed!\nExpected: {expected}\nActual: {list_price_after}"
        except Exception as e:
            self.logger.error(f"Sorting fail: {e}")
            self.attach_screenshot("Sorting with name (Z to A) fail")                         