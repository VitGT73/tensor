import time

import allure
from helpers.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SbisHeader(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
        # self.contacts_link = (By.XPATH, "//a[text()='Контакты']")
        # self.contacts_link = (By.XPATH, "//div[@class='sbisru-Header']//a[text()='Контакты']")

    def contacts_click(self):
        with allure.step(f"Переход в раздел 'Контакты'"):
            self.driver.find_element(self.CONTACTS_LINK).click()

    # def is_contacts_page_opened(self):
    #     with allure.step(f"Страница Контакты' открыта"):
    #         self.driver.find_element(self.contacts_link).click()
