import logging
import os
from datetime import datetime

os.makedirs('logs',exist_ok=True)
logs_file = os.path.join('logs', f"{datetime.now():%d_%m_%H_%M_%S}.log")

logging.basicConfig(
        filename=logs_file,
        format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
        datefmt='%d/%b/%Y %I:%M:%S %p',
        level=logging.INFO,
)

