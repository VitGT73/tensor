import allure
from helpers.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from POM.sections.sbis_header import SbisHeader

class SbisContactsPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.header = SbisHeader(driver)
        self.PAGE_URL = Links.SBIS_CONTACTS_PAGE
        self.TENSOR_BANNER = (By.XPATH, "(//a[@title='tensor.ru']//img)[1]")


    @allure.step("Click on 'My Info' link")
    def click_to_tensor_banner(self):
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER)).click()

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):

            self.wait.until(EC.url_contains(self.PAGE_URL))
            self.wait.until_not(EC.url_to_be(self.PAGE_URL))
