import os
from dotenv import load_dotenv

load_dotenv()

class Data:

    HOME_REGION = os.getenv("HOME_REGION")
    # LOGIN = os.getenv("LOGIN")
    # PASSWORD = os.getenv("PASSWORD")
