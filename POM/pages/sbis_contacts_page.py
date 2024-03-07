import time
import allure
from helpers.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from POM.sections.sbis_header import SbisHeader
from POM.sections.sbis_footer import SbisFooter


class SbisContactsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.header = SbisHeader(driver)
        self.footer = SbisFooter(driver)
        self.PAGE_URL = Links.SBIS_CONTACTS_PAGE
        self.TENSOR_BANNER = (By.XPATH, "(//a[@title='tensor.ru']//img)[1]")
        self.CHECKED_REGION = (
            By.XPATH,
            "//div[div[h2[text()='Контакты']]]//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']",
        )
        self.CHOICE_REGION = (By.XPATH, "//h5[text()='Выберите свой регион']")
        self.CHOICE_REGION_RENDERED = (By.XPATH, "//div[contains(@data-qa,'controls-Render')]")
        self.REGION_LINK_CSS_SELECTOR = 'span.sbis_ru-link[title*="{}"]'

        self.PARTNER = (By.ID, "city-id-2")


    def click_to_tensor_banner(self):
        with allure.step("Click to Tensor banner"):
            self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER)).click()

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_contains(self.PAGE_URL))
            self.wait.until_not(EC.url_to_be(self.PAGE_URL))

    def this_region_is_checked(self, region: str):
        with allure.step(f"Region '{region}' is checked"):
            self.wait.until(
                EC.text_to_be_present_in_element(self.CHECKED_REGION, region)
            )

    def open_regions_list(self):
        with allure.step("Open regions list"):
            self.wait.until(EC.element_to_be_clickable(self.CHECKED_REGION)).click()

    def is_region_list_loaded(self):
        with allure.step("Regions list is loaded"):
            self.wait.until(EC.presence_of_all_elements_located(self.CHOICE_REGION_RENDERED))
            self.wait.until(EC.presence_of_element_located(self.CHOICE_REGION))

    def click_region_link(self, region):
        with allure.step(f"Activate region '{region}'"):
            self.wait.until(EC.presence_of_all_elements_located(self.CHOICE_REGION_RENDERED))
            region_link_locator = (
                By.CSS_SELECTOR,
                self.REGION_LINK_CSS_SELECTOR.format(region),
            )
            self.wait.until(EC.element_to_be_clickable(region_link_locator)).click()

    def check_partner_city(self, city):
        with allure.step(f"Check change city of partner to '{city}'"):
            self.wait.until(EC.text_to_be_present_in_element(self.PARTNER, city))

    def check_title(self, region):
        with allure.step(f"Check title is contains '{region}'"):
            self.wait.until(EC.title_contains(region))

    def check_url(self, region):
        with allure.step(f"Check URL is contains '{region}'"):
            self.wait.until(EC.url_contains(region))
