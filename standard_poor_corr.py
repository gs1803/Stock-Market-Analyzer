import bs4 as bs
import datetime as dt
import pandas as pd
import requests
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import yfinance as yf
style.use('ggplot')

def save_sp500_tickers() -> list:
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        ticker = ticker[:-1]
        if "." in ticker:
            ticker = ticker.replace('.', '-')
        tickers.append(ticker)

    return tickers

def get_data_from_yahoo() -> None:
    tickers = save_sp500_tickers()

    start = dt.datetime(2015, 1, 1)
    end = dt.datetime(2022, 12, 1)

    dfs = []
    for ticker in tickers:
        df = yf.download(ticker, start, end, progress = False)
        df.rename(columns = {'Adj Close': ticker}, inplace = True)
        df.drop(columns = ['Open' ,'High', 'Low', 'Close', 'Volume'], axis = 1, inplace = True)
        dfs.append(df)

    main_df = pd.concat(dfs, axis = 1)
    main_df.to_csv('sp500_joined_closes.csv')

def visualize_data() -> None:
    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr(numeric_only = True)

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    heatmap = ax.pcolor(data, cmap = plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor = False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor = False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation = 90)
    heatmap.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()
