import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    PAGE_URL: str = 'https://sbis.ru'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)


    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)


    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            print('-actual_url: ', self.driver.current_url)
            print('-self.PAGE_URL: ', self.PAGE_URL )
            self.wait.until(EC.url_contains(self.PAGE_URL))


    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG,
        )



    def switch_to_self(self, original_window):
        with allure.step(f"Swith to {self.PAGE_URL} page"):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.number_of_windows_to_be(2))
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
