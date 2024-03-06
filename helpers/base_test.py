import pytest
from config.data import Data
from POM.pages.sbis_contacts_page import SbisContactsPage
from POM.pages.sbis_home_page import SbisHomePage
from POM.pages.sbis_download_page import SbisDownloadPage
from POM.pages.tensor_about_page import TensorAboutPage
from POM.pages.tensor_home_page import TensorHomePage


class BaseTest:

    data: Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.sbis_home_page = SbisHomePage(driver)
        request.cls.sbis_contacts_page = SbisContactsPage(driver)
        request.cls.sbis_download_page = SbisDownloadPage(driver)
        request.cls.tensor_home_page = TensorHomePage(driver)
        request.cls.tensor_about_page = TensorAboutPage(driver)
