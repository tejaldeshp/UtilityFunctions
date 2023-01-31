"""
This function drops all the columns and rows whose index is passed as parameters
Input:  df- dataframe to be manipulated (type = dataframe)
        skiprow- list of row indices to be skipped(type = list)
        skipcol- list of column indices to be skipped(type = list)
Output: dataframe
Call : df = SkipRowCol(df,skiprow=[0,3,5], skipcol=[3])
"""

import pandas as pd

def skipRowCol(df,skiprow=[], skipcol=[]):
    rows=df.index
    cols = df.columns
    if skiprow:
        df = df.drop([rows[x] for x in skiprow], axis="rows")
    if skipcol:
        df = df.drop([cols[x] for x in skipcol], axis="columns")
    return df