import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Outputs the main menu and checks the user input
def main_menu():
    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Total sales by product")
        print("2. Sales of different categories of products")
        print("3. Income and profit made on different products")
        print("4. Quit")

        choice = input('Enter your number selection here: ')

        if choice.isdigit():
            flag = False
        else:
            print("Please enter a number to select an option")
            flag = True

    return int(choice)

#Generates submenu of available product codes and allows user to select a product to view
def get_product_id ():

    df = pd.read_csv("Task4a_RetailX_data.csv")

    product_codes = df["Product ID"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        
        product_ID = product_codes[selection -1]
   
    print("You have selected product id:",product_ID)
    return product_ID

#gets and converts user input from string to date format
def get_date(start_end):
    
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return date

#extracts data based on product ID within a user specified date range.
def get_data_by_ID_and_date(product_id, start_date, end_date):
    all_data = pd.read_csv("Task4a_RetailX_data.csv")
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]



    return extracted_data

#generates a total of the number of items sold for the extracted data
def calculate_total_sale (date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(product_id, start_date, end_date, total_sales))

# Gets the product category from the data frame
def get_product_category():
    df = pd.read_csv("Task4a_RetailX_data.csv")

    product_categories = df["Category"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        j = 0
        for i in range(len(product_categories)):
            print(i+1, " ", product_categories[i])
            j = i+2
        print(j, "  All")
        

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            
            if selection <= len(product_categories) and selection > 0:
                flag = False
                local_product_category = product_categories[selection -1]
            elif selection == 4:
                local_product_category = "All"
                flag = False
            else:
                print("Please select a valid category")
        else:
            flag = True
   
    print("You have selected product id:", local_product_category)
    return local_product_category

# Filters dataframe to an extract for a specific product category between the two selected dates
def get_sales_by_category(product_category, start_date, end_date):
    all_data = pd.read_csv("Task4a_RetailX_data.csv")

    if product_category != "All":
        product_data = all_data.loc[all_data["Category"] == product_category].copy()
    else:
        product_data = all_data

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]

    return extracted_data

# Plots the graph for an appropriate graphical output for the end user
def plot_sales_category_graph(sales_df, product_category, start_date, end_date):
    plt.plot(sales_df["Date"],sales_df["Qty Sold"])
    plt.tight_layout()
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title('Sales for {} products, between {} and {}'.format(product_category, start_date, end_date))
    plt.grid()
    plt.show()

# Plots the graph for all categories which allows for further data comparisons, plots multiple lines
def plot_sales_graph(sales_df, start_date, end_date):
    product_categories = sales_df["Category"].unique().tolist()

    for category in product_categories:
        category_data = sales_df.loc[sales_df["Category"] == category].copy()
        plt.plot(category_data["Date"], category_data["Qty Sold"], label = category)
    
    plt.tight_layout()
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title('Sales for all products, between {} and {}'.format(start_date, end_date))
    plt.grid()
    plt.legend()
    plt.show()

def calculate_income_and_profit():
    df = pd.read_csv("Task4a_RetailX_data.csv")
    
    df["Income"] = df["Qty Sold"] * df["Sales Price"]

    df["Profit"] = df["Income"] - (df["Qty Sold"] * df["Cost Price"])

    groupedIncomeAndProfitObject = df.groupby(df["Product ID"])

    columnList = ["Income", "Profit"]

    groupedIncomeAndProfitObjectSum = groupedIncomeAndProfitObject[columnList].sum()

    df_extract = groupedIncomeAndProfitObjectSum.reset_index()

    print(df_extract)

    return df_extract

def plot_income_and_profit_graph(income_and_profit_df):
    x = np.arange(len(income_and_profit_df["Product ID"]))
    width = 0.4

    plt.bar(x - width/2, income_and_profit_df["Income"],width = width, label = "Income")
    plt.bar(x + width/2, income_and_profit_df["Profit"],width = width, label = "Profit")

    plt.ticklabel_format(style = "plain", axis = "y")

    plt.xticks(x, income_and_profit_df["Product ID"])
    plt.grid()
    plt.title("Income and profit for all products")
    plt.xlabel("Product")
    plt.ylabel("Money (£)")
    plt.legend()
    plt.show()

def main():
    while True:
        main_menu_choice = main_menu()

        # Branch for "Total sales by products" option
        if main_menu_choice == 1:
            product_id = get_product_id()
            start_date = get_date("start")
            end_date = get_date("end")
            date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
            calculate_total_sale (date_ID, product_id, start_date, end_date)

        # Branch for "Sales of different categories of products" option
        elif main_menu_choice == 2:
            product_category = get_product_category() 
            start_date = get_date("start")
            end_date = get_date("end")
            sales_df = get_sales_by_category(product_category, start_date, end_date)
            
            # Depending on the product category return value, selects a function to plot the appropriate graph
            if product_category != "All":
                plot_sales_category_graph(sales_df, product_category, start_date, end_date) 
            else:
                plot_sales_graph(sales_df, start_date, end_date)
        
        elif main_menu_choice == 3:
            income_and_profit_df = calculate_income_and_profit()
            plot_income_and_profit_graph(income_and_profit_df)
        
        elif main_menu_choice == 4:
            break
        else:
            print("Please enter a valid menu option")

main()

