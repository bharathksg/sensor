import logging
import os
from datetime import datetime

log_dir:str="logs"
os.makedirs(log_dir,exist_ok=True)

def get_log_file_name():
    return f"logs_{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}"

log_file_name=get_log_file_name()
log_file_path=os.path.join(log_dir,log_file_name)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s];%(levelname)s;%(message)s"   
)