import os,pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from abc import ABC,abstractmethod
from src.Logger import logging
from src.Exception_Handler import Custom_Excetption


"""
define the UniVariate_Analysis_Strategies as Abstrace class.
Abstract must define a initiate_analysis method as abstract method
Returns:
None -> plot ans print some basic information  like columsn types and min and max and frequency and sahpes and columns descriptions
"""
class Basic_Insights_analyze_Strategies(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def initiate_analysis(self,df :pd.DataFrame):
        """
        Preformed Analysis over data like finding shape, columns datatype columns description and null info and many more operation perfomred over here.
        Parameters:
        df ->(pd.DataFrame) it contains the data set.
        
        Returns:
        None -> Just print some information in  as EDA.
        
        """
        pass


#Concrete class  that defines the one of the Strategy named as Basic_Info_Strategy sub class Basic_Insights_analyze_Strategies
# must have or implement a function initiate_analysis

class Basic_Info_Strategy(Basic_Insights_analyze_Strategies):
    def __init__(self):
        super().__init__()
    def initiate_analysis(self, df: pandas.DataFrame):
        #print the shape of the dataset
        print(f"shape of the data set is :{df.shape}")
        print("*"*60)

        #show the some data set (5 rows(randomly), all columns)
        print("5 rows sample data look like this : \n")
        print(df.sample(5))
        print("*"*60)
        #prints the the duplicated values in the data set
        print(f"the total numbers of duplicated values in the dataset :{df.duplicated().sum()}")

        print("*"*60)
        #print the notnull and types of the column 
        print(f"the info about the data set is \n:{df.info()}")
        print("*"*60)

#Concrete class that defines another Strategy named as Statistical_Info_Strategy of base class Basic_Insights_analyze_Strategies.
# This class must defines a methos names as initiate_analysis()
class Statistical_Info_Strategy(Basic_Insights_analyze_Strategies):
    def __init__(self):
        super().__init__()

    def initiate_analysis(self, df: pandas.DataFrame):
        #print the Statistically information of the given dataset
        print("Statistical summary for numerical columns/features")
        print(df.describe())
        print("*"*60)
        print("Statistical summary for categorical columns/features ")
        print(df.describe(include="O"))


#Context class of abstract class name Basic_Insights_analyze_Strategies
# This class must implement a method name called as set_strategy for set the desired strategies of Basic_Insights_analyze_Strategies
# this class must implement a method name class execute_strategy for execute that selected strategy.

class Basic_Insights:
    def __init__(self,strategy:Basic_Insights_analyze_Strategies):
        self._strategy=strategy

    def set_strategy(self,strategy:Basic_Insights_analyze_Strategies):
        self._strategy=strategy


    def execute_strategy(self,df:pd.DataFrame):

        #This method execute the selected strategy methods.
        
        self._strategy.initiate_analysis(df)