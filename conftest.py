import pytest
from utils.browser_utils import BrowserUtils
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.fixture(scope='function')
    #Bình thường: Mỗi test method sẽ mở/đóng browser riêng biệt 
    #scope = 'class' => Sau khi tất cả test trong class chạy xong, browser mới được đóng lại. 
    #scope='function' => Mỗi test case có driver riêng -> An toàn, phù hợp khi dùng parametrize với data-driven test. 
def driver():                  
    browser_utils = BrowserUtils(browser_name="chrome") #use composition
    driver = browser_utils.open_browser()
    yield driver
    browser_utils.close_browser()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver) 
@pytest.fixture
def home_page(driver):
    return HomePage(driver)  