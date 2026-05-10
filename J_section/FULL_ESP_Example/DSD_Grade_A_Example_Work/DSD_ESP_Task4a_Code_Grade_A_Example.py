import pandas as pd
import matplotlib.pyplot as plt

def main_menu():
    flag = True

    while flag:
        print("######################################################")
        print("Welcome to the RBSX currency analysis tool")
        print("Please select an option")
        print("1. Calculate currency conversion")
        print("2. Compare GBP to other currencies")
        print("3. Currency performance analysis")
        print("")
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 3:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return menu_choice  
            
#The menu() function generates the UI the accepts and validates user choice
def menu1():

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Austrailan Dollars (AUD)")
        print("4. Austrailan Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("")
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-6): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 6:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return menu_choice  


#Gets the short version of the conversion information based on user menu choice
def get_currency (menu_choice):
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GPB - JPY',
       '6': 'JPY - GBP'}
   
    currency = currencies.get(menu_choice)
    
    return currency





#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate(currency):
    df = pd.read_csv("Task4a_RBSX_data.csv")
    
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate



#Accepts and validates user input for teh amount they want to convert
def get_amount_to_convert(currency):
    print("You are converting: ",currency)
    
    flag = True
    
    while flag:
        conversion_amount = input("please enter the ammount you wish to convert")
    
        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount  



#Performs the converison and outputs the final values
def perfom_conversion(conversion_amount, conversion_rate, currency):
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will recieve {} in {}'.format(amount_recieved, currency[6:9]))
    
#Gets the ussrrs choice of which currency they wish to use in their comparisons
def gbp_comparison ():
    flag = True
    
    while flag:
        print("Please select the currency you wish to compare to GBP:")
        print("1. Euros (EUR)")
        print("2. Austrailan Dollars (AUD)")
        print("3. Japanese Yen (JPY)")      
        print("###############################################")

        compare_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(compare_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(compare_choice) < 1 or int(compare_choice) > 3:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
               flag = False
        
    if compare_choice == "1":
        currency_header = "EUR - GBP"
    elif compare_choice == "2":
        currency_header = "AUD - GBP"
    else:
        currency_header = "JPY - GBP"

    return currency_header

#gets the user's selection of which currency they want to see performance data for and returns a string with with correct dtaaframe header
def currency_performance():
    flag = True
    
    while flag:
        print("Please select the currency you wish to see the perfomance of:")
        print("1. Euros (EUR)")
        print("2. Austrailan Dollars (AUD)")
        print("3. Japanese Yen (JPY)")      
        print("###############################################")

        compare_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(compare_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(compare_choice) < 1 or int(compare_choice) > 3:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
               flag = False
        
    if compare_choice == "1":
        currency_header = "EUR - GBP"
    elif compare_choice == "2":
        currency_header = "AUD - GBP"
    else:
        currency_header = "JPY - GBP"

    return currency_header

#extracts the headers from the csv file
def get_currency_headers():
    data = pd.read_csv("Task4a_RBSX_data.csv")
    currencies = list(data.columns.values)
    currencies.pop(0)
    return currencies

def get_compare_range():

    flag = True
    
    while flag:
        print("###############################################")
        print("###########   Historical data      ############")
        print("###############################################")
        print("Please choose a time fram for your comparison")
        print("1. Last 7 days")
        print("2. Last 14 days")
        print("3. Last 30 days")
        print("###############################################")

        range_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(range_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(range_choice) < 1 or int(range_choice) > 3:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return range_choice 
            
#Compares GBP to the selected curency
#provides a grpah f the data over the slected timeframe
#caluclates teh average exchange rate in the given time frame
def process_value_data(range,currency_header):
    
    main_df = pd.read_csv("Task4a_RBSX_data.csv")
    
    
    if range == "1":
        gbp_df = main_df[["Date",currency_header]]
        seven_day_gbp = gbp_df.iloc[-7:]
        seven_day_avg = round(seven_day_gbp[currency_header].mean(),3)
        seven_day_gbp.plot(x="Date", y = currency_header)
        plt.show()
        print("GBP to {} for the last 7 days".format(currency_header))
        print(seven_day_gbp)
        print("")
        print("The aveage convesion rate for the last 7 days is: ", seven_day_avg )

    elif range == 2:
        gbp_df = main_df[["Date", currency_header]]
        fourteen_day_gbp = gbp_df.iloc[-14:]
        fourteen_day_avg = round(fourteen_day_gbp[currency_header].mean(),3)
        fourteen_day_gbp.plot(x="Date", y = currency_header)
        plt.show()
        print("GBP to USD last 14 days")
        print(fourteen_day_gbp)
        print("")
        print("The aveage convesion rate for the last 14 days is: ", fourteen_day_avg )
    else:
        gbp_df = main_df[["Date", currency_header]]
        thirty_day_gbp = gbp_df.iloc[-30:]
        thirty_day_avg = round(thirty_day_gbp[currency_header].mean(),3)
        thirty_day_gbp.plot(x="Date", y = currency_header)
        plt.show()
        print("GBP to USD last 30 days")
        print(thirty_day_gbp)
        print("")
        print("The aveage convesion rate for the last 30 days is: ", thirty_day_avg )

#calculates the perfomance of a currency compared to GBP and identifies any increase or decrease in value
def process_perfomance_data(range,chosen_currency):
    
    main_df = pd.read_csv("Task4a_RBSX_data.csv")
    
    
    if range == "1":
        currency_df = main_df[["Date",chosen_currency]]
        seven_day_perf = currency_df.iloc[-7:]
        start = seven_day_perf[chosen_currency].iloc[1]
        end = seven_day_perf[chosen_currency].iloc[-1]
        variation = end - start
        print("The starting value of this currency compared to GBP is:",start)
        print("The final value of this currency compared to GBP is:",end)
        if variation > 0:
            print("This currency has increased in value over the last 7 days")
        elif variation < 0:
            print("This currency has decreased in value over the last 7 days")
        else:
            print("This currency has not changed in value over the last 7 days")
       
    elif range == 2:
        currency_df = main_df[["Date",chosen_currency]]
        seven_day_perf = currency_df.iloc[-14:]
        start = seven_day_perf[chosen_currency].iloc[1]
        end = seven_day_perf[chosen_currency].iloc[-1]
        variation = end - start
        print("The starting value of this currency compared to GBP is:",start)
        print("The final value of this currency compared to GBP is:",end)
        if variation > 0:
            print("This currency has increased in value over the last 14 days")
        elif variation < 0:
            print("This currency has decreased in value over the last 14 days")
        else:
            print("This currency has not changed in value over the last 14 days")
    else:
        currency_df = main_df[["Date",chosen_currency]]
        seven_day_perf = currency_df.iloc[-30:]
        start = seven_day_perf[chosen_currency].iloc[1]
        end = seven_day_perf[chosen_currency].iloc[-1]
        variation = end - start
        print("The starting value of this currency compared to GBP is:",start)
        print("The final value of this currency compared to GBP is:",end)
        if variation > 0:
            print("This currency has increased in value over the last 30 days")
        elif variation < 0:
            print("This currency has decreased in value over the last 30 days")
        else:
            print("This currency has not changed in value over the last 30 days")

def main():
    main_choice = main_menu()

    if main_choice == "1":
        menu_choice = menu1()
        currency = get_currency(menu_choice)
        conversion_rate = get_conversion_rate(currency)
        conversion_amount = float(get_amount_to_convert(currency))
        perfom_conversion(conversion_amount, conversion_rate, currency)
    elif main_choice == "2":
        
        currency_header = gbp_comparison()
        range = get_compare_range()
        process_value_data(range,  currency_header)
    
    elif main_choice == "3":
        chosen_currency = currency_performance()
        range = get_compare_range()
        process_perfomance_data(range,chosen_currency)

main()