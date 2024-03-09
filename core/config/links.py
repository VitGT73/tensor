
import os

class Links:
    # SBIS pages
    SBIS_HOST = "https://sbis.ru"
    SBIS_HOME_PAGE: str = f"{SBIS_HOST}"
    SBIS_CONTACTS_PAGE: str = f"{SBIS_HOST}/contacts"
    SBIS_DOWNLOAD_PAGE: str = f"{SBIS_HOST}/download"

    # Тензор pages
    TENSOR_HOST = "https://tensor.ru"
    TENSOR_HOME_PAGE: str = f"{TENSOR_HOST}"
    TENSOR_ABOUT_PAGE: str = f"{TENSOR_HOST}/about"

    # downloads path
    DOWNLOAD_PATH:str = os.getcwd() + "/downloads"

    # Home region
    HOME_REGION = 'Оренбургская обл.'
