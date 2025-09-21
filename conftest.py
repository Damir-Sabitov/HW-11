import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from tempfile import mkdtemp

@pytest.fixture(scope="function")
def setup_browser():
    options = Options()
    options.add_argument(f"--user-data-dir={mkdtemp()}")  # уникальная папка профиля

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
        desired_capabilities=capabilities
    )

    browser = Browser(Config(driver))
    yield browser
    browser.quit()