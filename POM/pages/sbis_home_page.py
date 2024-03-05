import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.sections.sbis_header import SbisHeader

class SbisHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.header = SbisHeader(driver)
        self.PAGE_URL = Links.SBIS_HOME_PAGE


    @allure.step("Click on 'Контакты' link")
    def click_to_contacts_link(self):
        self.wait.until(EC.element_to_be_clickable(self.header.contacts_link)).click()

