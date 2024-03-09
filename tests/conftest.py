import shutil
import os
import pytest
from selenium import webdriver
from core.config.links import Links

# Imports to get chrome driver working
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Imports to get firefox driver working
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session", autouse=True)
def remove_download_directory():
    # Путь к папке, которую нужно удалить
    directory_path = Links.DOWNLOAD_PATH

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

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # Setup
    print(f"\nSetting up: {browser} driver")
    if browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:
        preferences = {
            "download.default_directory": Links.DOWNLOAD_PATH,
        }
        options.add_experimental_option("prefs", preferences)

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    # Implicit wait setup for our framework
    driver.implicitly_wait(10)
    yield driver
    # Tear down
    print(f"\nTear down: {browser} driver")
    driver.quit()
