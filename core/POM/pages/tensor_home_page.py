import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from core.helpers.base_page import BasePage
from core.config.links import Links


class TensorHomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.PAGE_URL = Links.TENSOR_HOME_PAGE
        self.POWER_IN_PEOPLE = (By.XPATH, "//div[p[text()='Сила в людях']]")
        self.ABOUT = (
            By.XPATH,
            "//div[p[text()='Сила в людях']]//a[text()='Подробнее']",
        )

    def is_working_block_present(self):
        with allure.step("Block 'Сила в людях' is present"):
            self.wait.until(EC.presence_of_element_located(self.POWER_IN_PEOPLE))

    def is_details_present(self):
        with allure.step("Link 'Подробнее' is present"):
            self.wait.until(EC.element_to_be_clickable(self.ABOUT))

    def click_to_details_link(self):
        with allure.step("Click on 'Подробнее' link"):
            # Найти элемент, к которому нужно прокрутить страницу
            element = self.wait.until(EC.element_to_be_clickable(self.ABOUT))
            # Прокрутить страницу к нужному элементу
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
