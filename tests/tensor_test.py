import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helpers.base_test import BaseTest
from config.links import Links



@allure.title("Тестовое задание от компании Тензор")

class TestDefaultSuite(BaseTest):

    sbis_window = {}
    tenzor_window={}
    home_region = Links.HOME_REGION

    # @pytest.mark.skip
    @allure.description("Сравнение размеров картинок в блоке 'Работаем'")
    def test_first_scenario(self, driver):
        self.sbis_home_page.open()
        self.sbis_home_page.is_opened()
        self.sbis_home_page.click_to_contacts_link()
        self.sbis_contacts_page.is_opened()
        self.sbis_window = driver.current_window_handle
        self.sbis_contacts_page.click_to_tensor_banner()
        self.tensor_home_page.switch_to_self(self.sbis_window)
        self.tensor_window = driver.current_window_handle
        self.tensor_home_page.is_opened()
        self.tensor_home_page.is_working_block_present()
        self.tensor_home_page.is_details_present()
        self.tensor_home_page.click_to_details_link()
        self.tensor_about_page.is_opened()
        self.tensor_about_page.is_working_block_present()
        self.tensor_about_page.check_images_same_size()

    # @pytest.mark.skip
    @allure.description("Изменение региона на 'Камчатский край'")
    def test_second_scenario(self, driver):
        self.sbis_home_page.open()
        self.sbis_home_page.is_opened()
        self.sbis_home_page.click_to_contacts_link()
        self.sbis_contacts_page.is_opened()
        self.sbis_contacts_page.this_region_is_checked(self.home_region)
        self.sbis_contacts_page.open_regions_list()
        self.sbis_contacts_page.is_region_list_loaded()
        self.sbis_contacts_page.click_region_link('Камчатский край')
        self.sbis_contacts_page.this_region_is_checked('Камчатский край')
        self.sbis_contacts_page.check_partner_city('Петропавловск-Камчатский')
        self.sbis_contacts_page.check_title('Камчатский край')
        self.sbis_contacts_page.check_url('41-kamchatskij-kraj')

    @allure.description("Загрузка Sbis-plugin для Windows")
    def test_third_scenario(self, driver):
        self.sbis_home_page.open()
        self.sbis_home_page.footer.click_to_sbis_download_link()
        self.sbis_download_page.is_opened()
        self.sbis_download_page.click_to_plugin_link()
        self.sbis_download_page.is_plugin_section_open()
        download_path = self.sbis_download_page.download_web_installer()
        self.sbis_download_page.is_web_installer_have_right_size(download_path)
