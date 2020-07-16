# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 03:40:27 2020

@author: salma
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 02:32:39 2020

@author: salman
"""

import yfinance as yf
import streamlit as st

st.write("""
## Simple Stock Price App
Shown are the **stock closing price** and ***volume of Apple***!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AAP'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)