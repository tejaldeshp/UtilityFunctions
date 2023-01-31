"""
This function filters the dataframe as per the parameters provided 
Input:  df- dataframe to be manipulated (type = dataframe)
        filter_dict- dictionary of columns and their values to be filtered on (type = dict)
Output: dataframe
Call : df = dfFilter(df, filter_dict = {"SettlementPointName": "ALVIN_RN","SettlementPointType": "RN",})
"""

import pandas as pd

# filter_dict={
#   "SettlementPointName": "ALVIN_RN",
#   "SettlementPointType": "RN",
# }

# data_dict = {
#     "DeliveryDate": ["2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23","2022-01-23",],  
#     "DeliveryHour":[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23],  
#     "DeliveryInterval":[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,], 
#     "SettlementPointName":["AEEC","AJAXWIND_RN","ALGOD_ALL_RN","ALVIN_RN","AMADEUS_ALL","AMISTAD_ALL","AMOCOOIL_CC1","AMOCOOIL_CC2","AMOCO_PUN1","AMOCO_PUN2","AMO_AMOCO_1","AMO_AMOCO_2","AMO_AMOCO_5","AMO_AMOCO_G1","AMO_AMOCO_G2"], 
#     "SettlementPointType":["RN","RN","RN","RN","RN","RN","LCCRN","LCCRN","PUN","PUN","PCCRN","PCCRN","PCCRN","PCCRN","PCCRN",],  
#     "SettlementPointPrice":[20.15,20.15,20.15,20.15,20.15,20.15,20.15,20.15,20.15,20.15,20.15,20.15,20.15,20.15,20.15,], 
#     "DSTFlag":["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N",]       
# } 



def dfFilter(df, filter_dict):
    for k,v in filter_dict.items():
        df = df[df[k]==v]
    return df