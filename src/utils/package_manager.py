import importlib.util
import logging
import subprocess
import sys


def package_manager(package_name):
    spec = importlib.util.spec_from_file_location(package_name)
    if spec is not None:
        logging.info(f"Package available: {package_name}")
    else:
        logging.error(f"Package not available: {package_name}")
        try:
            logging.info(f"Try to install the package: {package_name}")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package_name]
            )
            print(f"'{package_name}' installed successfully.")
        except Exception as e:
            logging.error(f"Exception on installing the package")
            raise e

