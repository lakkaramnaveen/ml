import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App
""")
tickerSymbol = 'MSFT'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '1d', start='2010-5-31', end='2018-5-31')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)