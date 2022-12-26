import yfinance as yf
import pandas as pd
from tabulate import tabulate

class StockInformation:
    def __init__(self, stock) -> None:
        self.stock = yf.Ticker(stock)

    def stock_recommendations(self) -> None:
        try:
            analystRecom = self.stock.recommendations
            del analystRecom["From Grade"]
            headers_row = ['Date & Time', 'Firm', 'To Grade', 'Action']
            print(tabulate(analystRecom.tail(), headers = headers_row, tablefmt = 'psql'))
        except KeyError:
            print(" ")

    def stock_dividends(self) -> None:
        try:
            df_StockDiv = pd.DataFrame(self.stock.dividends)
            df_StockDiv.reset_index(inplace = True)
            df_StockDiv['Date'] = pd.to_datetime(df_StockDiv['Date']).dt.date
            headers_row = ['Date', 'Dividends']
            print(tabulate(df_StockDiv.tail(), headers = headers_row, tablefmt = 'psql', showindex = False))
        except KeyError:
            print(" ")

    def stock_splits(self) -> None:
        try:
            df_StockSpl = pd.DataFrame(self.stock.splits)
            df_StockSpl.reset_index(inplace = True)
            df_StockSpl['Date'] = pd.to_datetime(df_StockSpl['Date']).dt.date
            headers_row = ['Date', 'Splits']
            print(tabulate(df_StockSpl.tail(), headers = headers_row, tablefmt = 'psql', showindex = False))
        except KeyError:
            print(" ")

    def div_spl_chooser(self) -> None:
        while True:
            print("+------------------+")
            print("|d: Dividends      |")
            print("|s: Splits         |")
            print("|q: Quit to Menu   |")
            print("+------------------+")
            divSplOption = input("Select an option: ")

            if divSplOption == 'd':
                StockInformation.stock_dividends(self)
            elif divSplOption == 's':
                StockInformation.stock_splits(self)
            elif divSplOption == 'q':
                break
            else:
                print("Enter a valid option.")
