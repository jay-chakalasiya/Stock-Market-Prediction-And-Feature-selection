# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:42:48 2017

@author: JAY CHAKALSIYA
"""

from Indicators import EMA, MACD_Hist, SMA, TEMA, SIGNAL, PPO, RSI, AROON, OBV, STOS
from Date import DATEMAP, DATEPRICESLOP, DEVIATOR

#------------------------------------------------------------------------------------------------------------------------#

def DATAMAP (df):
    final_frame=df
    final_frame["Adj Close"] = df["Adj Close"].fillna(0)
    final_frame["EMA"] = EMA(df,26)
    final_frame["SMA"] = SMA(df,26)
    final_frame["TEMA"] = TEMA(df,20)
    final_frame["PPO"] = PPO(df)
    final_frame["MACD"] = MACD_Hist(df)
    final_frame["RSI"] = RSI(df)
    final_frame["AROON"] = AROON(df,25)
    final_frame["OBV"] = OBV(df)
    final_frame["STOS"] = STOS(df,14)
    
    final_frame["SIGNAL"] = SIGNAL(df)
    final_frame["MAPPED DATE"]=DATEMAP(df)
    
    Target_List=[0]
    i=0
    while i < len(final_frame)-1:
        Target_List.append(final_frame.iloc[i]["Adj Close"])
        i+=1
    final_frame["TARGET"] = Target_List
    return final_frame[1:-26]
    
#-----------------------------------------------------------------------------------------------------------------------#

def GENERATEFEED(df):
    feeddata = DATAMAP(df)
    
    indicator_list=["EMA","SMA","TEMA","PPO","MACD","RSI","OBV"]

    i=0
    while i<len(indicator_list):
        j=1
        while j <=10:
            feeddata[indicator_list[i]+str(j)]=DEVIATOR(feeddata,j,indicator_list[i])
            j=j+1
        i=i+1
        print(i)
    
    
    i=1
    while i <=10:
        feeddata["price_Date_slop"+str(i)]=DATEPRICESLOP(feeddata,i)   
        i=i+1
    
    
    return feeddata


