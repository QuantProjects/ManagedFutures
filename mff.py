import sys
import Quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dateutil.relativedelta as relativedelta
import risk_model as risk_model
from returns import get_returns
import factors as factors
from risk_model import get_cov
from factors import *


def backtest(startdate,enddate, strategy):
    
    dates= pd.date_range(startdate, enddate)
    
    # get returns and prices   
    df_prices, df_returns = get_returns()
    
       
    for date in dates:
        ## build cov 
        df_static_cov= risk_model.get_cov(df_returns, date)
        df_static_cov.to_clipboard()
        
        # build factor
        df_ret = factors.get_factor(df_prices,date)
        print df_ret
        
        #create_mom_3m_factor(df_prices)
    
        # build portfolio





class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    #
    
    backtest ("2014-1-1","2014-1-5", "")
     
    plt.show()
 

if __name__ == "__main__":
    sys.exit(main())