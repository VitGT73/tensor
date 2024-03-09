import time
import allure
from helpers.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SbisFooter(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.SBIS_DOWNLOAD_LINK = (By.LINK_TEXT, "Скачать локальные версии")

    def click_to_sbis_download_link(self):
        with allure.step("Open Sbis Download page"):
            time.sleep(1)
            element = self.wait.until(EC.element_to_be_clickable(self.SBIS_DOWNLOAD_LINK))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
