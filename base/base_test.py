import pytest
from config.data import Data
from POM.pages.sbis_contacts_page import SbisContactsPage
from POM.pages.sbis_home_page import SbisHomePage
from POM.pages.tenzor_about_page import TenzorAboutPage
from POM.pages.tenzor_home_page import TenzorHomePage


class BaseTest:

    data: Data

    # sbis_contacts_page: SbisContactsPage
    # sbis_home_page: SbisHomePage
    # tenzor_about_page:TenzorAboutPage
    # tenzor_home_page:TenzorHomePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.sbis_home_page = SbisHomePage(driver)
        request.cls.sbis_contacts_page = SbisContactsPage(driver)
        request.cls.tenzor_home_page = TenzorHomePage(driver)
        request.cls.tenzor_about_page = TenzorAboutPage(driver)
