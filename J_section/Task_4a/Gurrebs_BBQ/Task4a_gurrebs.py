import pandas as pd
import matplotlib.pyplot as plt

#Displays the main menu and collects choice of menu item
def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show lunch and dinner services for selected menu items")
        print("3. the menu item with the highest total and average sales within a specified time period")

        main_menu_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3

def get_sales_over_time(service, startdate, enddate, selected_item):
    df = pd.read_csv("Task4a_data.csv")
    df_service = df.loc[df["Service"] == service]
    df_menuitem = df_service.loc[df_service['Menu Item'] == selected_item]
    df_daterange = df_menuitem.loc[:,startdate:enddate]

    return df_daterange

     
main_menu = menu()
if main_menu == 1:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)

elif main_menu == 2:
    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()

    lunch_df = get_sales_over_time("Lunch", start_date, end_date, item).reset_index()
    dinner_df = get_sales_over_time("Dinner", start_date, end_date, item).reset_index()

    lunch_list = lunch_df.columns.tolist()[1:]
    dinner_list = dinner_df.columns.tolist()[1:]

    lunch_values = lunch_df.iloc[0, 1:].tolist()
    dinner_values = dinner_df.iloc[0, 1:].tolist()

    plt.plot(lunch_list, lunch_values, label = "Lunch")
    plt.plot(dinner_list, dinner_values, label = "Dinner")
    plt.legend()

    plt.show()




elif main_menu == 3:
    print("Third option under development")
