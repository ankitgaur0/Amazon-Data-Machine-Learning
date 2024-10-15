import os,sys
from datetime import datetime
import logging


# the root dir +Log (folder_name) + log_file_name(.log) -> log messages

root_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file_format=f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}.log"
Log_path=os.path.join(root_dir,"Log","log_file_format")
os.makedirs(Log_path,exist_ok=True)

Log_file_name=os.path.join(Log_path,log_file_format)

log_format="[%(asctime)s] %(levelname)s -%(name)s -%(filename)s :%(linenum)d -%(message)s"


logging.basicConfig(
    level=logging.INFO,
    filename=Log_file_name,
    format=log_format
)