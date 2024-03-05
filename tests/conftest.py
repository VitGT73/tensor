import pytest
from selenium import webdriver

# Imports to get chrome driver working
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Imports to get firefox driver working
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options


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

    # Option setup to run in headless mode (in order to run this in GH Actions)
    options = Options()
    # options.add_argument("--headless")
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
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    # Implicit wait setup for our framework
    driver.implicitly_wait(10)
    yield driver
    # Tear down
    print(f"\nTear down: {browser} driver")
    driver.quit()


# @pytest.fixture(scope="function", autouse=True)
# def driver(request):
#     options = Options()
#     # options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(options=options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
