import sys
import Quandl
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dateutil.relativedelta as relativedelta
import os as os

def get_cov(df_returns):
    
    df_cov=df_returns.cov()
    return df_cov
