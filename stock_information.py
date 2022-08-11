import yfinance as yf
import pandas as pd
from tabulate import tabulate

class StockInformation:
    def stock_recommendations(stock) -> None:
        try:
            stock = yf.Ticker(stock)
            analystRecom = stock.recommendations
            del analystRecom["From Grade"]
            headers_row = ['Date & Time', 'Firm', 'To Grade', 'Action']
            print(tabulate(analystRecom.tail(), headers = headers_row, tablefmt = 'psql'))
        except KeyError:
            print("Ticker is invalid")

    def stock_dividends(stock) -> None:
        try:
            stock = yf.Ticker(stock)
            df_StockDiv = pd.DataFrame(stock.dividends)
            df_StockDiv.reset_index(inplace=True)
            df_StockDiv['Date'] = pd.to_datetime(df_StockDiv['Date']).dt.date
            headers_row = ['Date', 'Dividends']
            print(tabulate(df_StockDiv.tail(), headers = headers_row, tablefmt = 'psql', showindex = False))
        except KeyError:
            print("Ticker is invalid.")

    def stock_splits(stock) -> None:
        try:
            stock = yf.Ticker(stock)
            df_StockSpl = pd.DataFrame(stock.splits)
            df_StockSpl.reset_index(inplace=True)
            df_StockSpl['Date'] = pd.to_datetime(df_StockSpl['Date']).dt.date
            headers_row = ['Date', 'Splits']
            print(tabulate(df_StockSpl.tail(), headers = headers_row, tablefmt = 'psql', showindex = False))
        except KeyError:
            print("Ticker is invalid.")

def div_spl_chooser(stock) -> None:
    while True:
        print("+------------------+")
        print("|d: Dividends      |")
        print("|s: Splits         |")
        print("|q: Quit to Menu   |")
        print("+------------------+")
        divSplOption = input("Select an option: ")
        if divSplOption == 'd':
            StockInformation.stock_dividends(stock)
        elif divSplOption == 's':
            StockInformation.stock_splits(stock)
        elif divSplOption == 'q':
            break
        else:
            print("Enter a valid option.")
