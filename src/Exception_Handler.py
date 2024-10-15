# this file defines the custom exception which return the message or linnumber and filename.
import os,sys
from pathlib import Path
from src.Logger import logging


class Custom_Excetption(Exception):
    def __init__(self,error_message,error_details:sys):
        #save the error message in error variable
        self.error=error_message

        #getting the error_details:sys info for getting iterate the filename and linenumber

        _,_,exc_tb=error_details.exc_info()
        #exc_tb -> treated as execute traceback object
        #iterate the lineumber from exc_tb variable
        self.linenumber=exc_tb.tb_lineno
        # iterate the file_name for exc_tb.tb_frame.f_code
        self.file_name=exc_tb.tb_frame.f_code.co_filename


    def __str__(self) -> str:
        return "Error Line Number is : [{0}] \n The file name is : [{1}] \n The error is : [{2}]".format(self.linenumber,self.file_name,str(self.error))

