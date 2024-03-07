import allure
from helpers.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.sections.sbis_header import SbisHeader
from POM.sections.sbis_footer import SbisFooter


class SbisHomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.header = SbisHeader(driver)
        self.footer = SbisFooter(driver)
        self.PAGE_URL = Links.SBIS_HOME_PAGE

    def click_to_contacts_link(self):
        with allure.step("Click on 'Контакты' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.header.CONTACTS_LINK)
            ).click()
