import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.sections.sbis_header import SbisHeader

class SbisContactsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.header = SbisHeader(driver)
        self.PAGE_URL = Links.SBIS_CONTACTS_PAGE
        self.TENZOR_BANNER = (By.XPATH, "(//a[@title='tensor.ru']//img)[1]")


    @allure.step("Click on 'My Info' link")
    def click_to_tenzor_banner(self):
        self.wait.until(EC.element_to_be_clickable(self.TENZOR_BANNER)).click()

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_contains(self.PAGE_URL))
