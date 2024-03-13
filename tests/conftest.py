from datetime import datetime
import time
import shutil
import os
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from core.config.settings import settings

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
    directory_path = settings.DOWNLOAD_PATH

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
    print("CI = ", settings.CI)
    print(f"\nSetting up: {browser} driver")
    if browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("-headless")
        # firefox_options.add_argument("--window-size=1920,1080")
        print('\nSELENIUM_GRID_USE: ', settings.SELENIUM_GRID_USE)
        if settings.SELENIUM_GRID_USE=='1':
            # For run in docker with Selenium Grid
            firefox_options.add_argument("--ignore-ssl-errors=yes")
            firefox_options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Remote(
                command_executor="http://selenium-hub:4444/wd/hub", options=firefox_options
            )
        else:
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()), options=firefox_options
            )
        driver.set_window_size(1920,1080)
    else:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        print('\nSELENIUM_GRID_USE: ', settings.SELENIUM_GRID_USE)
        if settings.SELENIUM_GRID_USE=='1':
            # For run in docker with Selenium Grid
            chrome_options.add_argument("--ignore-ssl-errors=yes")
            chrome_options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Remote(
                command_executor="http://selenium-hub:4444/wd/hub", options=chrome_options
            )
        else:
            # For run in Docker without Selenium Grid
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            # Setup

            preferences = {
                "download.default_directory": settings.DOWNLOAD_PATH,
            }
            chrome_options.add_experimental_option("prefs", preferences)

            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=chrome_options
            )

    # Implicit wait setup for our framework
    driver.implicitly_wait(10)
    yield driver
    # Tear down
    print(f"\nTear down: {browser} driver")
    driver.quit()

# Добавляем хук pytest_exception_interact, который вызывается при возникновении ошибки в тесте
def pytest_exception_interact(node, call, report):
    if report.failed:
        # Получаем доступ к драйверу (предполагая, что используется фикстура 'driver')
        driver = node.funcargs['driver']
        browser = driver.capabilities['browserName']
        time.sleep(1)
        # Создаем скриншот и прикрепляем его к отчету Allure
        allure.attach(
            driver.get_screenshot_as_png(),
            # name="screenshot",
            name=f"{browser}-screenshot {datetime.today()}",
            attachment_type=AttachmentType.PNG
        )
