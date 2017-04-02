# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:41:14 2017

@author: JAY CHAKALASIYA
"""

import pandas as pd
#from Indicators import RSI,AROON, STOS, OBV
from Dataset import GENERATEFEED

#"BHEL","BSE","CIPLA","GAIL",
companies_list = ["HDFC","HINCONST","HINDALCO","IOC","ITC","L&T","LUPIN","M&M","MTNL","NSE_from2007","ONGC","RELINFRA","SAIL","SBI","SUNPHARMA","TATAM","TATAP","WIPRO"]


i=0
while i < len(companies_list):
    file = pd.read_csv("Raw_Data/"+companies_list[i]+".csv")
    feed = GENERATEFEED(file)
    feed.to_csv("Processed2.0/"+companies_list[i]+".csv")
    print(i)
    i+=1




