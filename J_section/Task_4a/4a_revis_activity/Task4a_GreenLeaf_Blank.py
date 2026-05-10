
# GreenLeaf Café — Task 4a (2-hour version)
# ------------------------------------------
# Starter skeleton. You must extend this program
# to meet the system and user requirements.

import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "Task4a_GreenLeaf_data.csv"

def load_data():
    try:
        df = pd.read_csv(CSV_PATH)
    except FileNotFoundError:
        print("Error: Data file not found.")
        return None
    return df

def AverageInteractions():
    df = load_data()
    df["Total Interactions"] = df["Likes"] + df["Shares"] + df["Comments"]
    groupedPosts = df.groupby(["Post Category"])
    groupedAveragePosts = groupedPosts["Total Interactions"].mean().round(0)
    df2 = groupedAveragePosts.reset_index()
    print(df2)
    AverageInteractionsBarChart(df2)
    input("Press enter to move on")
    

def AverageInteractionsBarChart(df):
    barChart = plt.bar(df["Post Category"], df["Total Interactions"], color = "pink")
    barChart[df["Total Interactions"].idxmax()].set_color("red")
    plt.grid()
    plt.xlabel("Post Category")
    plt.ylabel("Total Interactions")
    plt.title("Average Total Interactions by Post Category")
    plt.show()

def BestDay():
    df = load_data() # Calls the function to load the dataframe

    # Creates a total interactions column, the values are likes shares and comments columns added together
    df["Total Interactions"] = df["Likes"] + df["Shares"] + df["Comments"]

    # Converts the date to the day of the week the date was on, and creates a new column for them
    df["Day Of Week"] = pd.to_datetime(df["Date"]).dt.day_name()

    # Group all the data for the days of the week together, so all the data is associated with one unique day
    groupedDays = df.groupby(["Day Of Week"])

    # Adds all the interactions to the days together and returns the totals for each day
    totalGroupedDays = groupedDays["Total Interactions"].sum()

    # Turns the groupedObject into a new dataframe, df2 is used as to not overwrite the existing dataframe for code security
    df2 = totalGroupedDays.reset_index()
    print(df2)

    # Finds the row with the highest total interactions and returns the index
    indexOfHighestDay = df2["Total Interactions"].idxmax()
    print(indexOfHighestDay)

    # Finds the day of the week using the index of the row with the highest totals from the above variable
    print(f"{df2["Day Of Week"].iloc[indexOfHighestDay]} had the highest interactions")
    input("Press enter to move on")

def main_menu():
    while True:
        print("#################################################")
        print("############## GreenLeaf Café ###################")
        print("#################################################")
        print("1) Average interaction data by Post Category")
        print("2) Best day of week for interactions")
        print("Q) Quit\n")
        choice = input("Enter your choice: ").strip()
        if choice.upper() == "Q":
            print("Goodbye!")
            break
        elif choice == "1":
            AverageInteractions()
        elif choice == "2":
            BestDay()
        else:
            print("Invalid choice, please try again.\n")

main_menu()
