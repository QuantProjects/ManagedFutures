import sys
import Quandl
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dateutil.relativedelta as relativedelta
import os as os

def get_returns():
    
    path = 'C:\\Users\\vishr_000\\Documents\\GitHub\\ManagedFutures'
    os.chdir(path)
    df_prices = DataFrame.from_csv('Futures Data.csv', header = 0)
    df_prices = df_prices.convert_objects(convert_numeric = True)
    df_prices = df_prices.replace(0,np.NaN)
    df_prices = df_prices.fillna(method = 'pad')
    
    df_returns = df_prices/df_prices.shift(1)
    
    returns_index = df_returns.cumprod()
    return df_prices,df_returns
    #returns_index.plot()
    #plt.show()
    

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
       
    get_returns()
    
    
    
 

if __name__ == "__main__":
    sys.exit(main())