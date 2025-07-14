import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()
        self.wait = WebDriverWait(self.driver, 10)
        
    # Login page element
    USERNAME_FIELD = (By.NAME, 'user-name')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    LOGIN_LOGO = (By.XPATH, '//div[@class="login_logo"]')
    
    # Home Page Elements
    HOME_LOGO = (By.XPATH, "//div[@class='app_logo']")
    BURGER_MENU = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')

    # Error Elements
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    
    def attach_screenshot(self, name="Screenshot"):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)    

    @allure.step("Navigate to login page")
    def navigate_to_login_page(self):
        self.logger.info("Navigating to login page: https://www.saucedemo.com/")
        self.driver.get('https://www.saucedemo.com/')
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        self.logger.info("Login page loaded successfully")

    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        self.logger.info(f"Entering username: {username}")
        username_field = self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        username_field.clear()
        username_field.send_keys(username)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.logger.info(f"Entering password: {'*' * len(password)}") #don't show password
        password_field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Click login button")
    def click_login_button(self):
        self.logger.info("Clicking login button")
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    @allure.step("Complete login process")
    def login(self, username, password):
        self.navigate_to_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Verify successful login")
    def is_login_successful(self):
        self.logger.info("Verifying login success")
        try:
            self.wait.until(EC.presence_of_element_located(self.HOME_LOGO))
            self.logger.info("Login successful - Home page logo found")
            return True
        except Exception as e:
            self.logger.error(f"Login failed: {e}")
            self.attach_screenshot("Login Failed")
            return False

    @allure.step("Verify home page logo is visible")
    def is_home_page_logo_visible(self):
        self.logger.info("Checking home page logo visibility")
        try:
            logo = self.wait.until(EC.presence_of_element_located(self.HOME_LOGO))
            is_visible = logo.is_displayed()
            logo_text = logo.text
            self.logger.info(f"Home page logo visible: {is_visible}, Text: {logo_text}")
            return is_visible and "Swag Labs" in logo_text
        except Exception as e:
            self.logger.error(f"Home page logo not found: {e}")
            self.attach_screenshot("Home Logo Not Found")
            return False

    # @allure.step("Verify current page is home page")
    # def is_on_home_page(self):
    #     self.logger.info("Verifying current page is home page")
    #     try:
    #         current_url = self.driver.current_url
    #         return "inventory" in current_url
    #     except Exception as e:
    #         self.logger.error(f"Error checking current page: {e}")
    #         return False

    @allure.step("Get error message")
    def get_error_message(self):
        self.logger.info("Getting error message if login fail")
        try:
            error_element = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
            error_text = error_element.text.strip()
            self.logger.info(f"Error message: {error_text}")
            return error_text
        except Exception as e:
            self.logger.error(f"No error message found: {e}")
            return ""
        
    @allure.step("Verify user remains on login page")
    def is_on_login_page(self):
        self.logger.info("Verifying current page is login page")
        try:
            current_url = self.driver.current_url
            return "inventory" not in current_url and "saucedemo.com" in current_url
        except Exception as e:
            self.logger.error(f"Error checking current page: {e}")
            return False
        
    @allure.step("Verify login form is visible")
    def is_login_form_visible(self):
        self.logger.info("Checking if login form is visible")
        try:
            username_field = self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
            password_field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD))
            return username_field.is_displayed() and password_field.is_displayed()
        except Exception as e:
            self.logger.error(f"Login form not visible: {e}")
            return False    
        
    @allure.step("Click burger menu")
    def click_burger_menu(self):
        self.logger.info("Clicking burger menu")
        burger_menu = self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU))
        burger_menu.click()

    @allure.step("Click logout button")
    def click_logout_button(self):
        self.logger.info("Clicking logout button")
        logout_button = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
        logout_button.click()

    @allure.step("Complete logout process")
    def logout(self):
        self.click_burger_menu()
        self.click_logout_button()

    @allure.step("Verify successful logout")
    def is_logout_successful(self):
        self.logger.info("Verifying logout success")
        try:
            self.wait.until(EC.presence_of_element_located(self.LOGIN_LOGO))
            self.logger.info("Logout successful - Login page logo found")
            return True
        except Exception as e:
            self.logger.error(f"Logout failed: {e}")
            self.attach_screenshot("Logout Failed")
            return False              
