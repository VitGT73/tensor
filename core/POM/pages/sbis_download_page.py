import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from core.helpers.base_page import BasePage
from core.helpers.file_utilites import file_download, get_file_size
from core.config.links import Links
from core.POM.sections.sbis_header import SbisHeader
from core.POM.sections.sbis_footer import SbisFooter


class SbisDownloadPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.header = SbisHeader(driver)
        self.footer = SbisFooter(driver)
        self.PAGE_URL = Links.SBIS_DOWNLOAD_PAGE

        self.PLUGIN_LINK = (By.XPATH, "//div[@data-id='plugin']")
        self.LINUX_TAB = (By.XPATH, "//div[@data-id='linux'][.//span[text()='Linux']]")
        self.WEB_INSTALLER_LINK = (
            By.XPATH,
            "//a[contains(text(),'Скачать (Exe 8.30 МБ)')]",
        )
        self.REPORT_URL_PART = "tab=ereport"
        self.PLUGIN_URL_PART = "tab=plugin"

    def click_to_contacts_link(self):
        with allure.step("Click on 'Контакты' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.header.CONTACTS_LINK)
            ).click()

    def click_to_plugin_link(self):
        with allure.step("Click on 'СБИС Плагин' link"):
            self.wait.until(EC.url_contains(self.REPORT_URL_PART))
            self.wait.until(EC.element_to_be_clickable(self.PLUGIN_LINK)).click()

    def is_plugin_section_open(self):
        with allure.step("Section Plugin is opened"):
            self.wait.until(EC.url_contains(self.PLUGIN_URL_PART))

    def click_to_linux_tab(self):
        with allure.step("Click on 'Linux' tab"):
            self.wait.until(EC.element_to_be_clickable(self.LINUX_TAB)).click()

    def is_linux_tab_open(self):
        with allure.step("Tab Linux is opened"):
            self.wait.until(
                EC.text_to_be_present_in_element_attribute(
                    self.LINUX_TAB, "class", "controls-Checked__checked"
                )
            )

    # def click_to_web_installer_download(self):
    #     with allure.step("Click to link for download web-installer"):
    #         self.wait.until(EC.element_to_be_clickable(self.WEB_INSTALLER_LINK)).click()

    def download_web_installer(self):
        with allure.step("Download web-installer"):
            element = self.wait.until(
                EC.visibility_of_element_located(self.WEB_INSTALLER_LINK)
            )

            file_url: str | None = element.get_attribute("href") if element else None
            fullname = file_download(file_url)
            return fullname

    def is_web_installer_have_right_size(self, download_path):
        with allure.step("Check size Web-installer file"):
            file_size = get_file_size(download_path)
            # print(file_size)
            assert file_size == 8699000, "Размер файла не соответствует 8.30 МБ"
