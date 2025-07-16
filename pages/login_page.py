import allure
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from pages.locators import login_locators as lo
from pages.locators import home_locators as ho

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()
        
    # locator
        self.username_field = page.locator(lo.USERNAME_FIELD)
        self.password_field = page.locator(lo.PASSWORD_FIELD)
        self.login_button = page.locator(lo.LOGIN_BUTTON)
        self.login_logo = page.locator(lo.LOGIN_LOGO)

        self.home_logo = page.locator(ho.HOME_LOGO)
        self.burger_menu = page.locator(ho.BURGER_MENU)
        self.logout_button = page.locator(ho.LOGOUT_BUTTON)
        self.error_message = page.locator(ho.ERROR_MESSAGE)

    @allure.step("Navigate to login page")
    def navigate_to_login_page(self):
        self.logger.info("Navigating to login page: https://www.saucedemo.com/")
        self.page.goto('https://www.saucedemo.com/')
        expect(self.username_field).to_be_visible()
        self.logger.info("Login page loaded successfully")

    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        self.logger.info(f"Entering username: {username}")
        self.username_field.fill(username)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.logger.info("Entering password")
        self.password_field.fill(password)

    @allure.step("Click login button")
    def click_login_button(self):
        self.logger.info("Clicking login button")
        self.login_button.click()

    @allure.step("Complete login")
    def login(self, username, password):
        self.navigate_to_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Verify login success")
    def is_login_successful(self):
        self.logger.info("Verifying login success")
        try:
            expect(self.home_logo).to_be_visible()
            return True
        except Exception as e:
            self.logger.error(f"Login failed: {e}")
            self.attach_screenshot("Login Failed")
            return False

    @allure.step("Check home page logo visible")
    def is_home_page_logo_visible(self):
        try:
            expect(self.home_logo).to_be_visible()
            logo_text = self.home_logo.inner_text()
            return "Swag Labs" in logo_text
        except Exception as e:
            self.logger.error(f"Home logo not visible: {e}")
            self.attach_screenshot("Home Logo Failed")
            return False

    @allure.step("Get error message")
    def get_error_message(self):
        try:
            expect(self.error_message).to_be_visible()
            return self.error_message.inner_text().strip()
        except Exception as e:
            self.logger.error(f"Error message not found: {e}")
            return ""

    @allure.step("Check if on login page")
    def is_on_login_page(self):
        return "inventory" not in self.page.url

    @allure.step("Login form should be visible")
    def is_login_form_visible(self):
        return self.username_field.is_visible() and self.password_field.is_visible()

    @allure.step("Click burger menu")
    def click_burger_menu(self):
        self.burger_menu.click()

    @allure.step("Click logout")
    def click_logout_button(self):
        self.logout_button.click()

    @allure.step("Complete logout")
    def logout(self):
        self.click_burger_menu()
        self.click_logout_button()

    @allure.step("Verify logout")
    def is_logout_successful(self):
        try:
            expect(self.login_logo).to_be_visible()
            return True
        except Exception as e:
            self.logger.error(f"Logout failed: {e}")
            self.attach_screenshot("Logout Failed")
            return False

    def attach_screenshot(self, name="Screenshot"):
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)