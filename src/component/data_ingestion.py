import logging
import os
from src.utils.common.common import download_data
import zipfile


class DataIngestion:

    def download_file(self):
        download_data('https://drive.google.com/uc?/export=download&id=1vlhZ5c7abUKF8xXERIw6m9Te8fW7ohw3', 'artifects/data/')

    def unzip_file(self):
        files_in_directory = os.listdir('artifects/data/')
        zip_files = [file for file in files_in_directory if file.endswith('.zip')]
        if zip_files:
            for file in zip_files:
                zip_path = os.path.join('artifects/data/' + file)
                extract_path = os.path.join('artifects/data/', os.path.splitext(file)[0])
                os.makedirs(extract_path, exist_ok=True)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
