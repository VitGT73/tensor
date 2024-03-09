import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from core.helpers.base_page import BasePage


class SbisHeader(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.CONTACTS_LINK = (By.LINK_TEXT, "Контакты")

    def contacts_click(self):
        with allure.step("Go to the 'Контакты' section"):
            self.wait.until(EC.element_to_be_clickable(self.CONTACTS_LINK)).click()
