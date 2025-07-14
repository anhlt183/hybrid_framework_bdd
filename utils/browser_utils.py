from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile

class BrowserUtils:
    def __init__(self, browser_name="chrome"):
        self.driver = None
        self.browser_name = browser_name

    def open_browser(self):
        # if self.browser_name == "chrome":
        #     self.driver = webdriver.Chrome()
        # elif self.browser_name == "firefox":
        #     self.driver = webdriver.Firefox()
        # else:
        #     raise Exception("Unsupported browser!")
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        # return self.driver
        if self.browser_name == "chrome":
            options = Options()
            options.add_experimental_option("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            })
            temp_profile = tempfile.mkdtemp()
            options.add_argument("--incognito")
            options.add_argument(f"--user-data-dir={temp_profile}")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--no-first-run")
            options.add_argument("--no-service-autorun")
            options.add_argument("--password-store=basic")
            options.add_argument("--disable-features=AutofillKeyedPasswords,PasswordManagerEnabled,PasswordManagerOnboarding,PasswordLeakDetection")
            self.driver = webdriver.Chrome(options=options)
        elif self.browser_name == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise Exception("Unsupported browser!")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.quit()