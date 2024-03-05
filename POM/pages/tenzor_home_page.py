import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TenzorHomePage(BasePage):

    PAGE_URL = Links.TENZOR_HOME_PAGE

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()
