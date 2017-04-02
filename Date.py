# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:48:13 2017

@author: JAY CHAKALASIYA
"""

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
    
  #----------------------------------------------------------------------------------------------------------------------------------------

def DATERANGE(first,last):
    last = last.split('-')
    first = first.split('-')
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    No_of_days=0
    start_year=int(first[0])
    end_year=int(last[0])
    start_month=int(first[1])
    end_month=int(last[1])
    start_day=int(first[2])
    end_day=int(last[2])

    cy=start_year
    cm=start_month
    cd=start_day
    i=0
    while i==0:
        if cy==end_year and cm==end_month and cd==end_day:
            i=1
        No_of_days+=1
        cd+=1
        if cm==2:
            if cy%4==0:
                if cd>29:
                    cm+=1
                    cd=1
            else:
                if cd>28:
                    cm+=1
                    cd=1
        else:
            if cd>days[cm-1]:
                cm+=1
                cd=1
        if cm>12:
            cy+=1
            if cy+1 < end_year:
                if cy%4==0:
                    No_of_days+=366
                else:
                    No_of_days+=365
                cy+=1
            cm=1
    return No_of_days
    
    
#---------------------------------------------------------------------------------------------------------------------------------------

# i is a difference between days on which the slop is counted 
# where it can't be applicable the default value is  0

def DATEPRICESLOP(df,i):    
    slop_list=[]
    j=0
    while j<i:
        slop_list.append(0.0)
        j=j+1
    
    j=len(df)-1-i
    while j>=0 :
        slop = (df.iloc[j]["Adj Close"] - df.iloc[j+i]["Adj Close"])/(df.iloc[j]["MAPPED DATE"]-df.iloc[j+i]["MAPPED DATE"])
        slop_list.append(slop)
        j=j-1
   
    slop_list.reverse()
        
    return slop_list
    
    
#---------------------------------------------------------------------------------------------------------------------------------------
# indicator deviator

def DEVIATOR(df,i,indicator):
    deviation_list = []

    j=0
    while j<i:
        deviation_list.append(0.0)
        j=j+1
        
    j=len(df)-1-i
    while j>=0 :
        deviation = (df.iloc[j][indicator] - df.iloc[j+i][indicator])*100/(df.iloc[j+i][indicator]*(df.iloc[j]["MAPPED DATE"]-df.iloc[j+i]["MAPPED DATE"]))
        #deviation = (df.iloc[j][indicator] - df.iloc[j+i][indicator])*100/df.iloc[j+i][indicator]
        deviation_list.append(deviation)
        j=j-1
    
    deviation_list.reverse()
        
    return deviation_list
              
        
        
    
   
    
