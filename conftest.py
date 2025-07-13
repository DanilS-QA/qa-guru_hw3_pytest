from selene import browser
import pytest

@pytest.fixture(scope='function')
def setting_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def browser_open():
    browser.open('https://bing.com/')
    yield
    browser.quit()