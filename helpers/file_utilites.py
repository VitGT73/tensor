import os

import requests
from config.links import Links

def get_filename_with_path(filename):
    return f"{Links.DOWNLOAD_PATH}/{filename}"

def get_file_size(fullname):
    file_size_bytes = os.path.getsize(fullname)
    print(file_size_bytes)
    return file_size_bytes

def get_filename_from_url(url):
    filename = url.split("/")[-1]
    return filename


def file_download(file_url):
    download_path: str = get_filename_with_path(get_filename_from_url(file_url))
    response = requests.get(file_url)

    if response.status_code == 200:
        os.makedirs(Links.DOWNLOAD_PATH)
        with open(download_path, 'wb') as file:
            file.write(response.content)
            # file_size = get_file_size(download_path)
        return download_path
    return None
