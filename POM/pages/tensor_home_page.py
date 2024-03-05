import allure
from helpers.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config.links import Links

class TensorHomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.PAGE_URL = Links.TENSOR_HOME_PAGE
        self.POWER_IN_PEOPLE = (By.XPATH, "//div[p[text()='Сила в людях']]")
        self.ABOUT = (By.XPATH, "//div[p[text()='Сила в людях']]//a[text()='Подробнее']")

    @allure.step("Блок 'Сила в людях' существует")
    def is_working_block_present(self):
        self.wait.until(EC.presence_of_element_located(self.POWER_IN_PEOPLE))

    @allure.step("Link 'Подробнее' is present")
    def is_details_present(self):
        self.wait.until(EC.element_to_be_clickable(self.ABOUT))

    @allure.step("Click on 'Подробнее' link")
    def click_to_details_link(self):
        # Найти элемент, к которому нужно прокрутить страницу
        element = self.driver.find_element(*self.ABOUT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.element_to_be_clickable(self.ABOUT)).click()
