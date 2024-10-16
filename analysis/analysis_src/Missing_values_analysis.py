# This file is used to analysis the missing values in data set and visualize them.
import os,sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.Exception_Handler import Custom_Excetption
from src.Logger import logging
from abc import ABC,abstractmethod


# The class name Missingvalues_analysis_Template react as abstract class.
# And should implement a method name analyze for execute the method like identifaction of missing values and visualizing the missing values in heatmap for better readbility.

class Missingvalues_analysis_Template(ABC):
    def analysis(self,df :pd.DataFrame):
        """
        This method contains the initializing method of identifaction of missing_values and visualizing them.

        # If we execute this method then, whole operations will be execute.
        """
        self.identify_missing_values(df)
        self.visualize_missing_values(df)


    @abstractmethod
    def identify_missing_values(self,df:pd.DataFrame):
        """
        Perfoms the identifaction of missing values (sum()) and print them in a well format.
        parameters:
        df ->(pd.DataFrame) this contains the data .
        Returns:
        None -> Just print the info about missing values with respect to the columns/features.
        """
        pass

    @abstractmethod
    def visualize_missing_values(self,df:pd.DataFrame):
        """
        Perfrom the visual representation of the missing values using heatmap graph.
        Parameters:
        df -> (pd.DataFrame) this contains the data for operations.
        Returns:
        None -> Just visualize the heatmap using the seaborn and matplotlib.pyplot
        
        """


        pass

#Concrete class of Missingvalues_analysis_Template abstract class.
#Perfroms or define the abstract method in this class of abstract class abstract method.
# 
class Missing_values(Missingvalues_analysis_Template):
    def __init__(self) -> None:
        super().__init__()


    def identify_missing_values(self, df: pd.DataFrame):
        # print the missing values with respect to the giving data.
        print("the missing values are : \n")
        df.isnull().sum()

        print("*"*60)

    def visualize_missing_values(self, df: pd.DataFrame):
        # Here visualize the missing values

        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(),cmap="viridis",cbar=False)
        plt.title("Missing values with heatmap")
        plt.show()

    