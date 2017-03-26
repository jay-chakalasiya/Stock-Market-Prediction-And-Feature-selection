import pandas as pd

from Dataset import GENERATEFEED
from Indicators import RSI,EMA


companies_list = ["M&M","MTNL","ONGC","RELINFRA","SAIL","SBI","SUNPHARMA","TATAM","TATAP","WIPRO"]
#"BHEL","CIPLA","GAIL","HDFC","HINCONST","HINDALCO","IOC","ITC","L&T","LUPIN",
"""
i=0
while i < len(companies_list):
    file = pd.read_csv("IndData/"+companies_list[i]+".csv")
    feed = GENERATEFEED(file[0:2000])
    feed.to_csv("PreProcessed/"+companies_list[i]+".csv")
    print(i)
    i=i+1
"""
file = pd.read_csv("IndData/M&M.csv")
test = RSI(file)
file["RSI"]=test
print(file)
#file["RSI"]=test
