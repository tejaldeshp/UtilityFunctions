"""
This function converts the the date and time columns or timestamp column into datetime/timestamp column.
Input:  df- dataframe to be manipulated (type = dataframe)
        dateCols- list of columns to convert to timestamp type (type = list)
Output: dataframe
Call : df = df = datetimeCol(df, dateCols=dateCols)
"""

import pandas as pd

def datetimeCol(df, dateCols=[]):
    if dateCols:
        df[dateCols] = df[dateCols].apply(pd.to_datetime)
    return df
