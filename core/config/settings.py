import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # downloads path
    DOWNLOAD_PATH: str = os.getcwd() + "/downloads"

    # Home region
    HOME_REGION = "Оренбургская обл."

    # LOGIN = os.getenv("LOGIN")
    # PASSWORD = os.getenv("PASSWORD")
