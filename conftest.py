import pytest
from utils.browser_utils import BrowserUtils

@pytest.fixture(scope='function')
    #Bình thường: Mỗi test method sẽ mở/đóng browser riêng biệt 
    #scope = 'class' => Sau khi tất cả test trong class chạy xong, browser mới được đóng lại. 
    #scope='function' => Mỗi test case có driver riêng -> An toàn, phù hợp khi dùng parametrize với data-driven test. 
def driver():                  
    browser_utils = BrowserUtils(browser_name="chrome") #use composition
    driver = browser_utils.open_browser()
    yield driver
    browser_utils.close_browser()