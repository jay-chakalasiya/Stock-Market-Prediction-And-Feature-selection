# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:42:48 2017

@author: JAY CHAKALSIYA
"""

from Indicators import EMA, MACD_Hist, SMA, TEMA, SIGNAL, PPO, DATERANGE, DATEPRICESLOP, DEVIATOR

#------------------------------------------------------------------------------------------------------------------------#

def DATAMAP (df):
    final_frame=df
    final_frame["Adj Close"] = df["Adj Close"].fillna(0)
    final_frame["EMA"] = EMA(df,26)
    final_frame["SMA"] = SMA(df,26)
    final_frame["TEMA"] = TEMA(df,20)
    final_frame["PPO"] = PPO(df)
    final_frame["MACD"] = MACD_Hist(df)
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


def DATEMAP(df):
    maximum = max(df["Adj Close"])
    minimum = min(df["Adj Close"])
    mapped_date_list=[]
    
    Adj_close_difference = maximum-minimum
    date_difference=DATERANGE(df.iloc[-1]["Date"],df.iloc[0]["Date"])
    
    multiplier = Adj_close_difference/date_difference
    constant = minimum+1
    
    i=0
    j=len(df)-1
    while i <= len(df)-1:
        mapped = constant + multiplier*DATERANGE(df.iloc[j]["Date"],df.iloc[j-i]["Date"])
        mapped_date_list.append(mapped)
        i+=1
        
    mapped_date_list.reverse()
    return mapped_date_list
        
    
#-----------------------------------------------------------------------------------------------------------------------#

def GENERATEFEED(df):
    feeddata = DATAMAP(df)
    
    indicator_list=["EMA","SMA","TEMA","PPO","MACD"]

    i=0
    while i<len(indicator_list):
        j=1
        while j <=10:
            feeddata[indicator_list[i]+str(j)]=DEVIATOR(feeddata,j,indicator_list[i])
            j=j+1
        i=i+1
    
    
    i=1
    while i <=10:
        feeddata["price_Date_slop"+str(i)]=DATEPRICESLOP(feeddata,i)   
        i=i+1
    
    
    return feeddata