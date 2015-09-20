import sys
import Quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dateutil.relativedelta as relativedelta

# Asset names
def get_asset_prices():
    asset_tags = ["YAHOO/INDEX_GSPC", "YAHOO/INDEX_HSI","YAHOO/INDEX_FCHI","YAHOO/INDEX_GDAXI","NIKKEI/INDEX","YAHOO/INDEX_FTSEMIB_MI","YAHOO/INDEX_GSPTSE","YAHOO/INDEX_IBEX","YAHOO/INDEX_STI"]
    
    asset_names= ["US","HK","FR","BD","JP","IT","CA","ES","SG"]
    
    # Get asset returns in a list of dataframes
    # for each day get 3m/1m/12m signals 
    # for each day build portfolio using singal
    # compute pnl for signal
    
    asset_prices = []
    
    
    for asset_tag in asset_tags:
        asset_prices_df = Quandl.get(asset_tag, authtoken="WnzSYJ9RpDF2HuzQ9pZ2")
        print asset_prices_df.column
        if "Adjusted Close" in asset_prices_df.columns:
            asset_prices.append(asset_prices_df["Adjusted Close"])
        else:
            asset_prices.append(asset_prices_df["Close Price"])
    
    df_prices =pd.concat(asset_prices , axis=1)
    df_prices.columns = asset_names
    df_prices=df_prices.truncate(before='1/1/2010', after='12/31/2014')
    
    df_returns = df_prices.pct_change()
    df_returns=df_returns.fillna(0)
    df_prices=df_prices.fillna(method='pad')
 
    
    return df_prices, df_returns

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
       
    df_prices, df_returns = get_asset_prices()
    create_mff_signal(df_prices,30)
    
    df_prices.plot()
    plt.show()
 

if __name__ == "__main__":
    sys.exit(main())