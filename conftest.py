import pytest
from selenium import webdriver
from selene import Browser, Config
from utils import attach


@pytest.fixture(scope='function')
def setup_browser(request):
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "latest",   # всегда актуальная версия
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=selenoid_capabilities
    )

    browser = Browser(Config(driver))
    yield browser

    # фиксация артефактов в Allure
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()