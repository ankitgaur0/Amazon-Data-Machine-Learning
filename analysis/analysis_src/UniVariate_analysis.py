import os,sys
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
None -> plot the graph for the numerical columns and categorical columns.
"""

class UniVariate_Analysis_Strategies(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def initiate_analysis(self,df :pd.DataFrame,feature_name :str):
        """
        Perform the analysis on top of single feature and column for finding the distribution of data and frequency of the data.
        DataFrame :
        df -> (pd.DataFrame) this contains the data as DataFrame.
        feature_name -> (string) name of the column name for visualize that.
        Returns:
        None -> plot the graph on top of individuals column data. 

        """
        pass

#Concrete class of UnVariate_Analysis_Strategies class.
# This class used for Numerical Features to find the distribuion of the data using seaborn and matplotlib tools.
# This class must implement and define the initiate_analysis method to analysis the data.
class Numerical_data_Strategy(UniVariate_Analysis_Strategies):
    def __init__(self):
        super().__init__()

    def initiate_analysis(self, df: pd.DataFrame, feature_name: str):
        # this function define to analysis the distribution of numerical data (type int64, float64).
        logging.info(f"distribution of the numerical feature :{feature_name} is creating.")
        plt.figure(figsize=(12,8))
        sns.displot(df[feature_name],bins=25,kde=True)
        plt.xlabel(f"distribution of feature {feature_name}")
        plt.ylabel("Frequeny")
        plt.show()


#Concrete class of UnVariate_Analysis_Strategies class.
# This class used for Numerical Features to find the distribuion of the data using seaborn and matplotlib tools.
# This class must implement and define the initiate_analysis method to analysis the data.
class Categorical_data_Strategy(UniVariate_Analysis_Strategies):
    def __init__(self):
        super().__init__()

    def initiate_analysis(self, df: pd.DataFrame, feature_name: str):
        # this function visualize the count plot and pie plot on a single feature if the feature have many category to repesent (like unique value) like provide the top and select categories.
        print("*"*60)
        print(f"total unique values are :{df[feature_name].unique}")
        print("*"*60)
        print(df[feature_name].value_counts())
        print("graph represention of value_counts")
        plt.figure(figsize=(10,6))
        sns.countplot(data=df,x=feature_name,orient="v",palette="muted")
        plt.title(f"Distribution of {feature_name}")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

# Context class named as UniVariate_Analysis .
# This is used for switching the Stragies of the  UniVariate_Analysis_Strategies class(child classes).

class UniVariate_Analysis:
    def __init__(self,strategy : UniVariate_Analysis_Strategies):
        """
        Perform the init functin used to initialzing the Abstract class and set a strategy on of them.
        Parameter:
        strategy -> type of UniVariate_Analysis_Strategies class (means one them a strategy).
        Returns:
        None -> store or assign the strategy to the variable name _strategy.
        """
        self._strategy=strategy

    def set_strategy(self,strategy:UniVariate_Analysis_Strategies):
        """
        Peform this function for changing ans switching the strategy of the UniVariate_Analysis_Strategies(child class -> stragy).
        Parameter:
        strategy -> treat as the strategy name that we have to switch.
        Returns:
        None -> Just switch the strategies.
        """
        self._strategy=strategy

    def execute_strategy(self,df:pd.DataFrame,feature_name :str):
        """
        Perform the execution of the switching the strategy by giving the parameters.
        Parameters:
        df (pd.DataFrame) -> this dataframe contains the entire data.
        freature_name (string) -> this is the feature /column name in the df data frame.
        Returns:
        None -> just execute the set strategy (initiate_analysi operation).

        """
        self._strategy.initiate_analysis(df,feature_name)