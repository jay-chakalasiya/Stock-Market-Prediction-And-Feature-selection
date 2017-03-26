# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:45:41 2017

@author: JAY CHAKALSIYA
"""

#indicators

# Date  should be given in the order as 0-highest and n-lowest order


def SIGNAL(df):
    BIASED_List = ["N/A"]
    Current_Index=0
    End_Index=len(df)-2
    
    while (Current_Index <= End_Index):
        if df.iloc[Current_Index]["Adj Close"] > df.iloc[Current_Index+1]["Adj Close"]:
            BIASED_List.append("BUY")
        else:
            BIASED_List.append("SELL")
        Current_Index+=1
   
    return BIASED_List
    
#---------------------------------------------------------------------------------------------------------------------------------------

def SMA(df, Time_Span):   #Simple Moving Average
    SMA_List=[]
    Current_Index=len(df)-1
    Start_Index = Current_Index - Time_Span+1
    End_Index=0
    Aggregate=0.0
    
    while Current_Index >= Start_Index:
        Aggregate += df.iloc[Current_Index]["Adj Close"]
        SMA_List.append(0.0)
        Current_Index -= 1
        
    SMA_List.pop()
    SMA_List.append(Aggregate)
    
    while Current_Index >= End_Index:
        SMA_Current = SMA_List[-1]+df.iloc[Current_Index]["Adj Close"]-df.iloc[Current_Index+Time_Span]["Adj Close"]
        SMA_List.append(SMA_Current)
        Current_Index-=1
    i=0
    while i < len(df) :
        SMA_List[i]=SMA_List[i]/Time_Span
        i+=1
    SMA_List.reverse()
    return SMA_List
 
#-----------------------------------------------------------------------------------------------------------------------------------
       
def PPO(df):              # Percentage Price Oscillator
    PPO_List=[]
    EMA_9_List = EMA(df,9)
    EMA_26_List = EMA(df,26)
    i=0
    
    while i<=len(df)-26:
        PPO_List.append((EMA_9_List[i]/EMA_26_List[i]-1)*100)
        i+=1
    i=0
    while i<25:
        PPO_List.append(0.0)
        i+=1
    
    return PPO_List
 
#-------------------------------------------------------------------------------------------------------------------------------------
    
def EMA(df, Time_Span):   # Exponential Moving Average - when data frame is given
    
    Current_Index = len(df)-1
    Start_Index = Current_Index - Time_Span + 1
    End_Index = 0
    Aggregate = 0.0
    EMA_List=[]
    
    while Current_Index >= Start_Index:
        Aggregate += df.iloc[Current_Index]["Adj Close"]
        EMA_List.append(0.0)
        Current_Index -= 1
        
    EMA_List.pop()    
    SMA = Aggregate/Time_Span
    EMA_List.append(SMA)
    Multiplier = 2/(Time_Span+1)
    
    while Current_Index >= End_Index:
        EMA_Current = (df.iloc[Current_Index]["Adj Close"] - EMA_List[-1])*Multiplier + EMA_List[-1]
        EMA_List.append(EMA_Current)
        Current_Index -= 1
    EMA_List.reverse()
    return EMA_List
    

def EMA_LS(ls, Time_Span):        # Exponential Moving Average - when a simple list is given
    Current_Index = len(ls)-1
    Start_Index = Current_Index - Time_Span + 1
    End_Index = 0
    Aggregate = 0.0
    EMA_LS_List=[]
    
    while Current_Index >= Start_Index:
        Aggregate += ls[Current_Index]
        EMA_LS_List.append(0.0)
        Current_Index -= 1
        
    EMA_LS_List.pop()    
    SMA = Aggregate/Time_Span
    EMA_LS_List.append(SMA)
    Multiplier = 2/(Time_Span+1)
    
    while Current_Index >= End_Index:
        EMA_Current = (ls[Current_Index] - EMA_LS_List[-1])*Multiplier + EMA_LS_List[-1]
        EMA_LS_List.append(EMA_Current)
        Current_Index -= 1
    EMA_LS_List.reverse()
    return EMA_LS_List  
#--------------------------------------------------------------------------------------------------------------------------------------

def MACD(df):    # Moving Average Convergence And Divergence
    MACD_List=[]
    EMA_12_List = EMA(df,12)
    EMA_26_List = EMA(df,26)
    
    i=0
    
    while i<= len(df)-26:
        MACD_List.append(EMA_12_List[i]-EMA_26_List[i])
        i+=1
    i=0
    while i < 25:
        MACD_List.append(0.0)
        i+=1

    return MACD_List

def MACD_Signal(df):             # MACD Signal Line
    MACD_Signal_List = EMA_LS(MACD(df),9)
    return MACD_Signal_List
    
def MACD_Hist(df):
    MACD_List = MACD(df)
    MACD_Signal_List = MACD_Signal(df)
    MACD_Hist_List=[]
    i=0
    while i < len(df):
        MACD_Hist_List.append(MACD_List[i]-MACD_Signal_List[i])
        i+=1
    return MACD_Hist_List
    
#-------------------------------------------------------------------------------------------------------------------------------------

def TEMA(df, Time_Span):  # Triple Exponential Moving Average
    TEMA_List=[]
    EMA_List = EMA(df, Time_Span)
    EMA_EMA_List = EMA_LS(EMA_List, Time_Span)
    EMA_EMA_EMA_List = EMA_LS(EMA_EMA_List,Time_Span)
    i=0
    while i < len(df):
        TEMA_List.append(3*(EMA_List[i]-EMA_EMA_List[i])+EMA_EMA_EMA_List[i])
        i+=1
    return TEMA_List

#-----------------------------------------------------------------------------------------------------------------------------------------
        
def RSI(df):    #Relative Strength Index
    RSI_List=[0]
    Avg_Gain=0
    Avg_Loss=0
    Current_Index=len(df)-2
    
    while len(df)-Current_Index <=14:
        RSI_List.append(0)
        if (df.iloc[Current_Index]["Adj Close"]-df.iloc[Current_Index+1]["Adj Close"]) > 0:
            Avg_Gain = (df.iloc[Current_Index]["Adj Close"]-df.iloc[Current_Index+1]["Adj Close"])/14
        else:
            Avg_Loss = (df.iloc[Current_Index+1]["Adj Close"]-df.iloc[Current_Index]["Adj Close"])/14
        Current_Index=Current_Index-1
    
    while Current_Index>=0:
        if (df.iloc[Current_Index]["Adj Close"]-df.iloc[Current_Index+1]["Adj Close"]) > 0:
            Avg_Gain = (Avg_Gain*13+df.iloc[Current_Index]["Adj Close"]-df.iloc[Current_Index+1]["Adj Close"])/14
        else:
            Avg_Gain = (Avg_Gain*13)/14

        if (df.iloc[Current_Index]["Adj Close"]-df.iloc[Current_Index+1]["Adj Close"]) < 0:
            Avg_Loss = (Avg_Loss*13+df.iloc[Current_Index+1]["Adj Close"]-df.iloc[Current_Index]["Adj Close"])/14
        else:
            Avg_Loss = (Avg_Loss*13)/14

            
        RSI_List.append(100*(1-(1/(1+(Avg_Gain/Avg_Loss)))))   
        Current_Index=Current_Index-1
    RSI_List.reverse()
    return RSI_List
    
#----------------------------------------------------------------------------------------------------------------------------------------
    
def STOS(df,per):    #%K indicator, Not %D
    dflen = len(df)
    k_list=[]
    for j in range(per):
        k_list.append(0)
    i=dflen
    while (i-per) > 0:
        hmax = max(df.iloc[i-per:i]["High"])
        lmin = min(df.iloc[i-per:i]["Low"])
        cl = df.iloc[i-per]["Close"]
        k_list.append(((cl - lmin)/(hmax - lmin))*100)
        #print(hmax,lmin,cl)
        i-=1
        
    k_list.reverse()
    return k_list
 
#----------------------------------------------------------------------------------------------------------------------------------------

def OBV(df):
    dflen = len(df)
    o_list=[]
    o_list.append(0)
    prev_obv=0
    i=dflen-2
    while i > -1:
        curr_cl = df.iloc[i]["Close"]
        prev_cl = df.iloc[i+1]["Close"]
        curr_vol = df.iloc[i]["Volume"]
        
        if curr_cl > prev_cl :
            curr_obv = prev_obv + curr_vol 
        elif curr_cl < prev_cl :
            curr_obv = prev_obv - curr_vol
        else:
            curr_obv = prev_obv
        o_list.append(curr_obv)
        prev_obv = curr_obv
        
        i-=1
    
    o_list.reverse()
    return o_list
    
