import pytest
from utils.browser_utils import BrowserUtils

@pytest.fixture(scope='function', autouse=True)
    #Bình thường: Mỗi test method sẽ mở/đóng browser riêng biệt 
    #scope = 'class' => Sau khi tất cả test trong class chạy xong, browser mới được đóng lại. 
    #scope='function' => Mỗi test case có driver riêng -> An toàn, phù hợp khi dùng parametrize với data-driven test. 
def setup(self, request):                                    #request là fixture đặc biệt của pytest, giúp bạn truy cập vào class test hiện tại.
    self.browser_utils = BrowserUtils(browser_name="chrome") #use composition
    self.driver = self.browser_utils.open_browser()
    request.cls.driver = self.driver     #Gán driver vào thuộc tính class, để tất cả test method trong class có thể dùng self.driver.
    yield
    self.browser_utils.close_browser()