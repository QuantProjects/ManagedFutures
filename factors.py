import sys
import Quandl
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dateutil.relativedelta as relativedelta
import os as os

def get_factor(df_prices, date):
    prev_date = date - relativedelta.relativedelta(years=1)
    
    #print (df_prices.index)   
    
    if prev_date.to_datetime() in df_prices.index and date.to_datetime() in df_prices.index:
        df_signal = (df_prices.ix[date.to_datetime()]/ df_prices.ix[prev_date.to_datetime()])-1  
        
    else:
        df_signal = np.NaN    
     
    return df_signal

def create_mom_3m_factor(df_prices, date):
    
    
    start_date = date - relativedelta.relativedelta(years=1)
    
    period = 90 #days
    start_date = df_prices.index[1]
    end_date = df_prices.index[-1]
    
    df_mff_signal = pd.DataFrame(index=df_prices.index, columns=df_prices.columns)
    df_mff_signal = df_mff_signal.fillna(0) # with 0s rather than NaNs
    
    for date in df_prices.index:
        prev_date=date - relativedelta.relativedelta(days=period)
        if prev_date in df_prices.index:
            df_mff_signal.ix[date]= (df_prices.ix[date] /df_prices.ix[prev_date])-1
        else:
            df_mff_signal.ix[date]= np.NaN
        
    
    df_mff_signal = df_mff_signal[np.invert(pd.isnull(df_mff_signal).any(axis=1))]
    
    df_mff_signal.plot()
    plt.show()
