import os,sys
from setuptools import setup,find_packages
from pathlib import Path
from typing import List

HYPEN_E_DOT="-e ."

def get_requirements_packages(requirement_path :str) -> List[str]:
    requirement_list=[]
    """
    requirement_list stores the library or packages names that has written in Requirements.txt.
    parameter : requirement_path is string or name is the path of the Requirementst.txt file
    Returns:
    return the list which stores the names of packages

    """
    if requirement_path !="":
        file_path=Path(requirement_path)

        with open(file_path,"r") as file:
            #read all the lines

            requirement_list=file.readlines()

        #readlines() function also stores the escape line \n element with packages names
        requirement_list=[a.replace("\n","") for a in requirement_list]

        # we have "-e ." parameter in the list , so remove this
        if HYPEN_E_DOT in requirement_list:
            requirement_list=requirement_list.remove(HYPEN_E_DOT)
        
    else: 
        print("please provide the Requirements.txt file path")








setup(

    name="Amazon_sales_analysis",
    version="0.0.1",
    author="Ankit_Gaur",
    author_email="ankitparashar000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements_packages("Requirements.txt")
)