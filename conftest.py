import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)
@pytest.fixture
def home_page(page):
    return HomePage(page)
@pytest.fixture
def product_detail_page(page):
    return ProductDetailPage(page)