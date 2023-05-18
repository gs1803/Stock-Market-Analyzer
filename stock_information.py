import pandas as pd
from tabulate import tabulate

class StockInformation:
    def __init__(self, stock) -> None:
        self.stock = stock

    def stock_major_holders(self) -> None:
        try:
            majorHolders = self.stock.major_holders
            headers_row = ['Percentage', 'Information']
            majorHolders = majorHolders.reset_index(drop = True)
            print(tabulate(majorHolders.values, headers = headers_row, tablefmt = 'psql'))
        except KeyError:
            print(" ")

    def stock_institutional_holders(self) -> None:
        try:
            institutionalHolders = self.stock.institutional_holders
            headers_row = ['Holder', 'Shares', 'Date Reported', '% Out', 'Value']
            institutionalHolders = institutionalHolders.reset_index(drop = True)
            print(tabulate(institutionalHolders.values, headers = headers_row, tablefmt = 'psql'))
        except KeyError:
            print(" ")

    def stock_mutualfund_holders(self) -> None:
        try:
            mutualfundHolders = self.stock.mutualfund_holders
            headers_row = ['Holder', 'Shares', 'Date Reported', '% Out', 'Value']
            mutualfundHolders = mutualfundHolders.reset_index(drop = True)
            print(tabulate(mutualfundHolders.values, headers = headers_row, tablefmt = 'psql'))
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

    def holder_chooser(self) -> None:
        while True:
            print("+--------------------------+")
            print("|m: Major Holders          |")
            print("|i: Institutional Holders  |")
            print("|f: Mutual Fund Holders    |")
            print("|q: Quit to Menu           |")
            print("+--------------------------+")
            holderOption = input("Select an option: ")

            if holderOption == 'm':
                StockInformation.stock_major_holders(self)
            elif holderOption == 'i':
                StockInformation.stock_institutional_holders(self)
            elif holderOption == 'f':
                StockInformation.stock_mutualfund_holders(self)
            elif holderOption == 'q':
                break
            else:
                print("Enter a valid option.")
