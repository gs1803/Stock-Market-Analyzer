import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib import style
import matplotlib.dates as mdates
import yfinance as yf
style.use("ggplot")

class StockAnalyzer:
    def __init__(self, stock, titleStock) -> None:
        self.stock = stock
        self.titleStock = titleStock
        self.companyStock = yf.Ticker(titleStock)
        
    def stock_prices(self) -> None:
        self.stock['Open'].plot(figsize = (15, 7))
        plt.title(f"Stock Prices for {self.titleStock} ({self.companyStock.info['shortName']})")
        plt.show()

    def stock_volume(self) -> None:
        self.stock['Volume'].plot(figsize = (15, 7))
        plt.title(f"Volume of Stock Traded of {self.titleStock} ({self.companyStock.info['shortName']})")
        plt.show()

    def stock_market_cap(self) -> None:
        self.stock['MktCap'] = self.stock['Open'] * self.stock['Volume']
        self.stock['MktCap'].plot(figsize = (15, 7))
        plt.title(f"Market Cap for {self.titleStock} ({self.companyStock.info['shortName']})")
        plt.show()

    def stock_moving_average(self) -> None:
        self.stock['MA50'] = self.stock['Open'].rolling(50).mean()
        self.stock['MA200'] = self.stock['Open'].rolling(200).mean()
        self.stock['Open'].plot(label = 'Open', figsize = (15, 7))
        self.stock['Adj Close'].plot(label = 'Adj Close')
        self.stock['MA50'].plot(label = '50 Days')
        self.stock['MA200'].plot(label = '200 Days')
        plt.legend()
        plt.title(f"Moving Average for {self.titleStock} ({self.companyStock.info['shortName']})")
        plt.show()
    
    def stock_volatility(self) -> None:
        self.stock['returns'] = (self.stock['Close'] / self.stock['Close'].shift(1)) -1
        self.stock['returns'].hist(bins = 100, alpha = 0.5, figsize = (15, 7))
        plt.title(f"Volatility of {self.titleStock} ({self.companyStock.info['shortName']})")
        plt.show()

    def stock_candlestick_graph(self) -> None:
        plt.figure(figsize = (15, 7))
        dS_ohlc = self.stock['Adj Close'].resample('10D').ohlc()
        dS_volume = self.stock['Volume'].resample('10D').sum()

        dS_ohlc.reset_index(inplace = True)
        dS_ohlc['Date'] = dS_ohlc['Date'].map(mdates.date2num)

        ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan = 5, colspan = 1)
        ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan = 1, colspan = 1, sharex = ax1)
        ax1.xaxis_date()

        candlestick_ohlc(ax1, dS_ohlc.values, width = 6, colorup = 'g')
        ax2.fill_between(dS_volume.index.map(mdates.date2num), dS_volume.values, 0)

        plt.title(f"Candlestick Graph for {self.titleStock} ({self.companyStock.info['shortName']})")
        plt.tight_layout()
        plt.show()

    def option_chooser(self) -> None:
        print('+---------------------+')
        print('|1: Prices            |')
        print('|2: Volume            |')
        print('|3: Market Cap        |')
        print('|4: Moving Average    |')
        print('|5: Volatility        |')
        print('|6: Candlestick Graph |')
        print('|q: Quit to Menu      |')
        print('+---------------------+')
        while True: 
            userDesicion = input("Select an option (1) (2) (3) (4) (5) (6) (q): ")

            if userDesicion == '1':
                StockAnalyzer.stock_prices(self)
            elif userDesicion == '2':
                StockAnalyzer.stock_volume(self)
            elif userDesicion == '3':
                StockAnalyzer.stock_market_cap(self)
            elif userDesicion == '4':
                StockAnalyzer.stock_moving_average(self)
            elif userDesicion == '5':
                StockAnalyzer.stock_volatility(self)
            elif userDesicion == '6':
                StockAnalyzer.stock_candlestick_graph(self)
            elif userDesicion == 'q':
                break
            else:
                print("Enter a valid option.")
                continue
