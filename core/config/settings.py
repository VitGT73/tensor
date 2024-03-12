import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # downloads path
    DOWNLOAD_PATH: str = os.getcwd() + "/downloads"

    # Home region
    HOME_REGION = "Оренбургская обл."

    # Use browsers from Selenium grid Docker
    SELENIUM_GRID_USE = os.getenv("SELENIUM_GRID_USE")


    # LOGIN = os.getenv("LOGIN")
    # PASSWORD = os.getenv("PASSWORD")

settings = Settings()
