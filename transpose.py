"""
This function transforms the dataframe's columns to rows and vice versa
Input:  df- dataframe to be manipulated (type = dataframe)
Output: dataframe
Call : df = 
"""

import pandas as pd

def transpose(df):
    return df.T