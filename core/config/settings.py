import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # downloads path
    CI = os.getenv("CI")
    DOWNLOAD_PATH: str = os.getcwd() + "/downloads"

    # Home region
    if CI == "1":
        HOME_REGION ="г. Москва"
    else:
        HOME_REGION = "Оренбургская обл."

    # Use browsers from Selenium grid Docker
    SELENIUM_GRID_USE = os.getenv("SELENIUM_GRID_USE")


    # LOGIN = os.getenv("LOGIN")
    # PASSWORD = os.getenv("PASSWORD")

settings = Settings()
