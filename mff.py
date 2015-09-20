import sys
import Quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dateutil.relativedelta as relativedelta
from returns import get_returns
from risk_model import get_cov

def create_mff_signal(df_prices, period):
    #computer  signal
    period = 30 #days
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

def backtest(signals):
    x=1

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
       
    df_prices, df_returns = get_returns()
    create_mff_signal(df_prices,30)
    
     
    plt.show()
 

if __name__ == "__main__":
    sys.exit(main())