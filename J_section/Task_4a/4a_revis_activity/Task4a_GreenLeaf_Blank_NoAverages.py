
# GreenLeaf Café — Task 4a (2-hour version, NO averages)
# -------------------------------------------------------
# Starter skeleton. You must extend this program
# to meet the system and user requirements.
#
# Requirements:
#   1) Show total interactions per Post Category
#   2) Show day of week with highest total interactions
#   3) Display a bar chart of total interactions by Post Category

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

def show_totals_by_category(df):
    print("\nTotal Likes, Shares, and Comments by Post Category:\n")
    df = df.copy()
    df["Total"] = df["Likes"] + df["Shares"] + df["Comments"]
    totals = df.groupby("Post Category")[["Likes","Shares","Comments","Total"]].sum()
    print(totals.to_string())
    print()

def show_best_day(df):
    print("\nDay of week with the highest total interactions:\n")
    df = df.copy()
    df["Total"] = df["Likes"] + df["Shares"] + df["Comments"]
    df["DayOfWeek"] = pd.to_datetime(df["Date"]).dt.day_name()
    totals = df.groupby("DayOfWeek")["Total"].sum()
    best_day = totals.idxmax()
    best_value = totals.max()
    print(f"{best_day} had the most interactions overall ({best_value}).\n")

def plot_bar_chart(df):
    df = df.copy()
    df["Total"] = df["Likes"] + df["Shares"] + df["Comments"]
    totals = df.groupby("Post Category")["Total"].sum()
    totals.plot(kind="bar", title="Total Interactions by Post Category")
    plt.ylabel("Total Interactions")
    plt.show()

def main_menu(df):
    while True:
        print("#################################################")
        print("############## GreenLeaf Café ###################")
        print("#################################################")
        print("1) Total interactions by Post Category")
        print("2) Best day of week for interactions")
        print("3) Bar chart of total interactions by Post Category")
        print("Q) Quit\n")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            show_totals_by_category(df)
        elif choice == "2":
            show_best_day(df)
        elif choice == "3":
            plot_bar_chart(df)
        elif choice.upper() == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        main_menu(df)
