import sys
import os
# Automatically add the project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.browser_utils import BrowserUtils
from pages.login_page import LoginPage
from pages.home_page import HomePage
# khoi tao trinh duyet
def before_all(context):
    context.browser = BrowserUtils(browser_name="chrome")  # bạn có thể thay bằng "firefox" nếu cần
    context.driver = context.browser.open_browser()
    context.login_page = LoginPage(context.driver)
    context.home_page = HomePage(context.driver)

def after_all(context):
    context.browser.close_browser()