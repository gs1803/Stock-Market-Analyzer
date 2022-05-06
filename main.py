from datetime import date
import yfinance as yf
from stock_analyzer import option_chooser
from industry_sorter import IndustrySorter

def stock_info() -> None:
    start = str(input("Enter the start time in (yyyy-mm-dd) format: "))
    end = date.today().strftime("%Y-%m-%d")
    try:
        userStock = input("Enter the Stock Ticker: ").upper()
        inputStock = yf.download(f"{userStock}", start, end, progress = False)
        option_chooser(inputStock, userStock)
    except ValueError:
        print("Enter a valid ticker.")

def industry_info() -> None:
    IndustrySorter.stock_details()

def main() -> None:
    while True:
        print("+----------------+")
        print("|g: View Graphs  |")
        print("|t: View Tickers |")
        print("|q: Quit         |")
        print("+----------------+")
        selectMainOpt = input("Select an option (g) (t) (q): ")
        if selectMainOpt == 'g':
            stock_info()
        elif selectMainOpt == 't':
            industry_info()
        elif selectMainOpt == 'q':
            break
        else:
            print("Enter a valid option.")
            continue

if __name__ == "__main__":
    main()
