from datetime import date
import yfinance as yf
from stock_analyzer import StockAnalyzer
from industry_sorter import IndustrySorter
from stock_information import StockInformation
from standard_poor_corr import visualize_data

def stock_info() -> None:
    start = str(input("Enter the start time in (yyyy-mm-dd) format: "))
    end = date.today().strftime("%Y-%m-%d")
    try:
        userStock = input("Enter the Stock Ticker: ").upper()
        inputStock = yf.download(f"{userStock}", start, end, progress = False)
        if inputStock.empty:
            pass
        else:
            infoStock = StockAnalyzer(inputStock, userStock)
            StockAnalyzer.option_chooser(infoStock)
    except ValueError:
        print("Enter a valid ticker.")

def industry_info() -> None:
    IndustrySorter.stock_details()

def holder_info() -> None:
    try:
        userStock = input("Enter the Stock Ticker: ").upper()
        holderStock = StockInformation(yf.Ticker(userStock))
        StockInformation.holder_chooser(holderStock)
    except ValueError:
        print("Enter a valid ticker.")

def div_or_split() -> None:
    try:
        userStock = input("Enter the Stock Ticker: ").upper()
        divSplitStock = StockInformation(yf.Ticker(userStock))
        StockInformation.div_spl_chooser(divSplitStock)
    except ValueError:
        print("Enter a valid ticker.")

def corr_table() -> None:
    visualize_data()

def main() -> None:
    while True:
        print("")
        print("+-----------------------+")
        print("|       Main Menu       |")
        print("+-----------------------+")
        print("|g: View Graphs         |")
        print("|t: View Tickers        |")
        print("|h: Holders Info        |")
        print("|i: Dividends and Splits|")
        print("|c: Correlation Table   |")
        print("|q: Quit                |")
        print("+-----------------------+")
        selectMainOpt = input("Select an option (g) (t) (h) (i) (c) (q): ")
        if selectMainOpt == 'g':
            stock_info()
        elif selectMainOpt == 't':
            industry_info()
        elif selectMainOpt == 'h':
            holder_info()
        elif selectMainOpt == 'i':
            div_or_split()
        elif selectMainOpt == 'c':
            corr_table()
        elif selectMainOpt == 'q':
            break
        else:
            print("Enter a valid option.")
            continue

if __name__ == "__main__":
    main()
