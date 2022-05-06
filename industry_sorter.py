import pandas as pd
from tabulate import tabulate

class IndustrySorter:
    def industry_list() -> None:
        names_head = ['Company Name', 'Ticker', 'Industry']
        data = pd.read_csv("stock_details.csv", encoding = 'utf-8', usecols = names_head, index_col = None)
        df = pd.DataFrame(data)

        df_sort = sorted(df['Industry'])
        test_df_sort = set(df_sort)
        df_tab = sorted(test_df_sort)

        industry_filter = input("Filter industries by alphabet (A-Z), (quit) to return to menu: ")
        running = True
        while running:
            list_dne = ['j', 'k', 'q', 'v', 'y', 'z']
            if industry_filter in list_dne:
                print("No industries starting with that letter.")
                break
            elif industry_filter == 'quit':
                running = False
            else:
                alpha_list = [element for element in df_tab if element.startswith(f"{industry_filter}")]
                df_alpha_list = pd.DataFrame({'Industry Name': alpha_list})
                df_alpha_list.set_index('Industry Name')
                print(tabulate(df_alpha_list, showindex = False,tablefmt = 'psql'))
                break

    def stock_details():
        names = ['Company Name', 'Ticker', 'Industry']
        data = pd.read_csv("stock_details.csv", encoding = 'utf=8', header = 0, index_col = 1)
        df = pd.DataFrame(data)

        flag = True
        while flag:
            print("+-------------------+")
            print("|t: View by Ticker  |")
            print("|i: View by Industry|")
            print("|q: Quit to menu    |")
            print("+-------------------+")
            detailChoose = input("Select an option: ")

            if detailChoose == 't':
                details = input("Enter the Ticker for the Stock (q to exit): ").upper()
                if details == 'Q':
                    break
                elif (df[df['Ticker'] == details].empty):
                    print("The Ticker you entered does not exist")
                    print("+---------------------+")
                    print("|q: Quit to menu      |")
                    print("|v: View more details |")
                    print("+---------------------+")
                    ticker_choices = input("Select an option: ")

                    if ticker_choices == 'v':
                        continue
                    
                    else:
                        flag = False

                else:
                    detail_stock = (df[df['Ticker'] == details])
                    print(tabulate(detail_stock, headers = names, tablefmt = 'psql'))

            elif detailChoose == 'i':
                chooseFilter = input("Would you like to view a list of the industries? (y/n): ")

                while flag:
                    if chooseFilter == "y":
                        IndustrySorter.industry_list()
                        break

                    else:
                        industryChoice = input("Enter an industry name (q to quit): ").lower()
                        if industryChoice == 'q':
                            break
                        elif (df[df['Industry'] == industryChoice].empty):
                            print("The industry you entered does not exist")
                            print("+---------------------+")
                            print("|q: Quit to menu      |")
                            print("|v: View more details |")
                            print("+---------------------+")
                            industry_choices = input("Select an option: ")
                            if industry_choices == 'v':
                                continue

                            else:
                                flag = False
                        else:
                            detailIndustry = (df[df['Industry'] == industryChoice])
                            print(tabulate(detailIndustry, headers = names, tablefmt = 'psql'))

            elif detailChoose == 'q':
                flag = False

            else:
                print("Enter a valid option.")
