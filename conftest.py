import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach

SELENOID_URL = "https://user1:1234@selenoid.autotests.cloud/wd/hub"

@pytest.fixture(scope='function')
def setup_browser(request):
    # Создаём временную уникальную папку для user-data-dir
    user_data_dir = tempfile.mkdtemp()

    options = Options()
    options.add_argument(f"--user-data-dir={user_data_dir}")  # уникальный профиль
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-allow-origins=*")

    # Selenoid capabilities
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "latest",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    driver = webdriver.Remote(
        command_executor=SELENOID_URL,
        options=options,
        desired_capabilities=capabilities
    )

    browser = Browser(Config(driver))
    yield browser

    # Сбор артефактов
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()