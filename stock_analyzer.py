import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib import style
import matplotlib.dates as mdates
style.use("ggplot")

class StockAnalyzer:
    def stock_prices(stock, titleStock) -> None:
        stock['Open'].plot(figsize = (15, 7))
        plt.title(f"Stock Prices for {titleStock}")
        plt.show()

    def stock_volume(stock, titleStock) -> None:
        stock['Volume'].plot(figsize = (15, 7))
        plt.title(f"Volume of Stock Traded of {titleStock}")
        plt.show()

    def stock_market_cap(stock, titleStock) -> None:
        stock['MarktCap'] = stock['Open'] * stock['Volume']
        stock['MarktCap'].plot(figsize = (15, 7))
        plt.title(f"Market Cap for {titleStock}")
        plt.show()

    def stock_moving_average(stock, titleStock) -> None:
        stock['MA50'] = stock['Open'].rolling(50).mean()
        stock['MA200'] = stock['Open'].rolling(200).mean()
        stock['Open'].plot(label = 'Open', figsize = (15, 7))
        stock['Adj Close'].plot(label = 'Adj Close')
        stock['MA50'].plot(label = '50 Days')
        stock['MA200'].plot(label = '200 Days')
        plt.legend()
        plt.title(f"Moving Average for {titleStock}")
        plt.show()
    
    def stock_volatility(stock, titleStock) -> None:
        stock['returns'] = (stock['Close']/stock['Close'].shift(1)) -1
        stock['returns'].hist(bins = 100, alpha = 0.5, figsize = (15, 7))
        plt.title(f"Volatility of {titleStock}")
        plt.show()

    def stock_candlestick_graph(stock, titleStock) -> None:
        plt.figure(figsize = (15, 7))
        dS_ohlc = stock['Adj Close'].resample('10D').ohlc()
        dS_volume = stock['Volume'].resample('10D').sum()

        dS_ohlc.reset_index(inplace = True)
        dS_ohlc['Date'] = dS_ohlc['Date'].map(mdates.date2num)

        ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan = 5, colspan = 1)
        ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan = 1, colspan = 1, sharex = ax1)
        ax1.xaxis_date()

        candlestick_ohlc(ax1, dS_ohlc.values, width = 6, colorup = 'g')
        ax2.fill_between(dS_volume.index.map(mdates.date2num), dS_volume.values, 0)

        plt.title(f"Candlestick Graph for {titleStock}")
        plt.tight_layout()
        plt.show()


def option_chooser(stock, titleStock) -> None:
    print('+---------------------+')
    print('|1: Prices            |')
    print('|2: Volume            |')
    print('|3: Market Cap        |')
    print('|4: Moving Average    |')
    print('|5: Volatility        |')
    print('|6: Candlestick Graph |')
    print('|q: Quit              |')
    print('+---------------------+')
    while True: 
        userDesicion = input("Select an option (1) (2) (3) (4) (5) (6) (q): ")
        if userDesicion == '1':
            StockAnalyzer.stock_prices(stock, titleStock)
        elif userDesicion == '2':
            StockAnalyzer.stock_volume(stock, titleStock)
        elif userDesicion == '3':
            StockAnalyzer.stock_market_cap(stock, titleStock)
        elif userDesicion == '4':
            StockAnalyzer.stock_moving_average(stock, titleStock)
        elif userDesicion == '5':
            StockAnalyzer.stock_volatility(stock, titleStock)
        elif userDesicion == '6':
            StockAnalyzer.stock_candlestick_graph(stock, titleStock)
        elif userDesicion == 'q':
            break
        else:
            print("Enter a valid option.")
            continue
