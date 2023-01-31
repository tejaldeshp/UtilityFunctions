"""
This function resamples the data based on input param like frequency and aggregation funtion.
Input:  df- dataframe to be manipulated having datetime-like index or add on parameter (type = dataframe)
        param- dictionary of freq and function to be carried out while resampling (type = dict)
        on- dataframe's date columnname to resample on(type=string)
Output: dataframe
Call : df = resample(df,param={"freq":"D","function"="mean"}) or df = resample(df,param={"freq":"D","function"="mean"}, on="fordate") 
"""



import pandas as pd
import numpy as np


# param ={
#     "freq":"D",
#     "function":np.mean
# }

def resample(df,param, on=None):
    grp_cols = [x for x in df.columns if df[x].dtype == "O"]
    if df.index.dtype == "datetime64[ns, UTC]":
        index= df.index.name
        df = df.groupby(grp_cols).resample(param["freq"]).aggregate(param["function"], numeric_only = True)
        df.reset_index(inplace=True)
        df.set_index(index, inplace=True)
    elif on:
        df = df.groupby(grp_cols).resample(param["freq"], on=on).aggregate(param["function"], numeric_only = True)
        df.reset_index(inplace=True)
    return df


# check this function out again