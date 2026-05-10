import pandas as pd
import matplotlib.pyplot as plt

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

        try:
            choice = int(input('Enter your number selection here: '))

            if choice < 4 and choice > 0:
                flag = False
            else: 
                flag = True
        
        except ValueError:
            print("Please enter a valid integer")

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


        try:
            selection = int(input('Enter your number selection here: '))

            if selection < 9 and selection > 0:
                product_ID = product_codes[selection - 1]
                flag = False
            else: 
                print('Please enter a valid number')
                flag = True
        
        except ValueError:
            print("Please enter a valid integer")
        
        
    print("You have selected product id:",product_ID)
    return product_ID


def get_product_id_2 ():

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
        j = 0
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])
            j = i+2
        print(j, "  All")

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        if selection == 10:
            product_ID = df['Product ID']
            print("You have selected all products")
            flag = False
        else:
            product_ID = product_codes[selection -1]

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
def get_product_caregory ():

    df = pd.read_csv("Task4a_RetailX_data.csv")

    product_category = df["Category"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        j = 0
        for i in range(len(product_category)):
            print(i+1, " ", product_category[i])
            j = i+2
        print(j, "  All")

        try:
            selection = input('Enter your number selection here: ')

            if selection.isdigit():
                selection = int(selection)
                flag = False
            else:
                flag = True

            if selection == 4:
                product_category = df['Category']
                print("You have selected all products")
                flag = False
            else:
                product_category = product_category[selection -1]
        except Exception:
            flag = True
            print(print("Please enter a valid integer"))

    return product_category



def get_data_by_category_and_date(product_category, start_date, end_date):
    all_data = pd.read_csv("Task4a_RetailX_data.csv")
    product_data = all_data.loc[all_data["Category"] == product_category].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]



    return extracted_data



def category_sales_graph(date_category, product_category):
    sales_per_day = date_category.groupby("Date")["Qty Sold"].sum()

    x = sales_per_day.index
    y = sales_per_day.values

    # Plot graph
    plt.figure(figsize=(10,5))
    plt.plot(x, y, marker='o', label='Qty Sold')

    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title(f'Sales of {product_category}')

    plt.grid()
    plt.legend()
    plt.tight_layout()

    plt.show()



def income_and_profit():

    sales = date_ID['Sales Price']
    qty = date_ID['Qty Sold']
    cost = date_ID['Cost Price']

    income = sales * qty
    profit = (sales - cost) * qty

    x = date_ID['Product ID']

    plt.bar(x, income, label='Income', width = 0.4)
    plt.bar(x, profit, label='Profit', width = 0.2)
    plt.title(f'Income and profit made on {product_id} from {start_date} to {end_date}')
    plt.xlabel('Product Name')
    plt.ylabel('Price')
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
    



main_menu_choice = main_menu()

if main_menu_choice == 1:
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_sale (date_ID, product_id, start_date, end_date)

elif main_menu_choice == 2:
    product_category = get_product_caregory()
    start_date = get_date("start")
    end_date = get_date("end")
    date_category = get_data_by_category_and_date(product_category, start_date, end_date) # Get dates from user
    graphs = category_sales_graph(date_category, product_category)

elif main_menu_choice == 3:
    product_id = get_product_id_2()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    Result = income_and_profit()




   


