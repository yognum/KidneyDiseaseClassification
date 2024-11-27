import os
import logging

from typing import Union, Tuple, Annotated
from pathlib import Path
from src.utils.package_manager import package_manager
import gdown


def download_data(url: str, path: str) -> None:
    # package_manager("gdown")
    gdown.download(url, output=path, quiet=False)
