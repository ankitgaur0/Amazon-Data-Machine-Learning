import os,sys
from pathlib import Path
import zipfile
from src.Logger import logging
from src.Exception_Handler import Custom_Excetption

project_directory=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file_path=os.path.join(project_directory,"Data","zip_file_data","amazone-phone-sales-prices.zip")
ouput_file_path=os.path.join(project_directory,"Data","processed_data","unzip_data")

class Unzip_data:
    def __init__(self):
        pass

    def initating_unzip(self):
        try:
            if os.path.exists(input_file_path):

                logging.info("open the zip file with zipfile function")
                with zipfile.ZipFile(input_file_path,"r") as zip_ref:
                    zip_ref.extractall(ouput_file_path) 

            else:
                print("please input the existing data zip file path")
                logging.info("zip file is not exists in the provided path")
        except Exception as e:
            raise Custom_Excetption(e,sys)
        

        

