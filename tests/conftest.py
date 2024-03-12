import shutil
import os
import pytest
from selenium import webdriver
from core.config.settings import Settings

# Imports to get chrome driver working
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Imports to get firefox driver working
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="session", autouse=True)
def remove_download_directory():
    # Путь к папке, которую нужно удалить
    directory_path = Settings.DOWNLOAD_PATH

    # Удаление папки, если она существует
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        print(f"\nПапка {directory_path} успешно удалена перед началом тестов.")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Send 'chrome' or 'firefox' as parameter for execution",
    )


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    crome_options = ChromeOptions()
    crome_options.add_argument("--headless")
    crome_options.add_argument("--window-size=1920,1080")
    print('\nSELENIUM_GRID_USE: ', Settings.SELENIUM_GRID_USE)
    if Settings.SELENIUM_GRID_USE=='1':
        # For run in docker with Selenium Grid
        crome_options.add_argument("--ignore-ssl-errors=yes")
        crome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub", options=crome_options
        )
    else:
        # For run in Docker
        crome_options.add_argument("--no-sandbox")
        crome_options.add_argument("--disable-dev-shm-usage")
               # Setup
        print(f"\nSetting up: {browser} driver")
        if browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("-headless")
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()), options=firefox_options
            )
        else:
            preferences = {
                "download.default_directory": Settings.DOWNLOAD_PATH,
            }
            crome_options.add_experimental_option("prefs", preferences)

            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=crome_options
            )

    # Implicit wait setup for our framework
    driver.implicitly_wait(10)
    yield driver
    # Tear down
    print(f"\nTear down: {browser} driver")
    driver.quit()
