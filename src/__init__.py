import os
import sys
import logging

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)


logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('cnnClassifierLogger')
