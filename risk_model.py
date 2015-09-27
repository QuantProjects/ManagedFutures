import sys
import Quandl
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dateutil.relativedelta as relativedelta
import os as os
import math

def get_cov(df_returns, date):
    
    cov_start_date = date - relativedelta.relativedelta(years=1)
    df_cov = df_returns.truncate(after=date, before = cov_start_date).cov() * math.sqrt(252)
    #df_cov=df_returns.cov()
    return df_cov
