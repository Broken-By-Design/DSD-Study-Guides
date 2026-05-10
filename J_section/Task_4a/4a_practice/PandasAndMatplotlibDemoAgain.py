import pandas as pd
import matplotlib.pyplot as plt

# Calculate and shows the average temperature and precipitation
def CalculateAverageTempAndPrec():
    df = pd.read_csv("WeatherData.csv")
    startDate = GetDates()
    endDate = GetDates()
    df_dateRange = []

    # Convert Date column to datetime to b e used in conditions
    df["Date"] = pd.to_datetime(df["Date"])

    # Loop used to filter a new dataframe with just the date range specified by the user
    for index, row in df.iterrows():
        if startDate <= row["Date"] <= endDate:
            df_dateRange.append(row)
    
    df_dateRange = pd.DataFrame(df_dateRange)
    print(df_dateRange)

    avgTemp = df_dateRange["Temperature (C)"].mean()
    print(f"The average temperature was {avgTemp} degrees celsius")

# Reused by functions that require dates
def GetDates():
    while True:
        try: 
            userDate = input("Enter date: ")
            userDate = pd.to_datetime(userDate)
            return userDate
        except:
            print("Date invalid")

# Displays the dates with the highest and lowest temperature and precipitation
def LowestAndHighestValues():
    df = pd.read_csv("WeatherData.csv")
    highestTempIndex = df["Temperature (C)"].idxmax()
    print(f"The date with the highest temperature was {df["Date"].iloc[highestTempIndex]} at {df["Temperature (C)"].iloc[highestTempIndex]} degrees celsius")
    lowestTempIndex = df["Temperature (C)"].idxmin()
    print(f"The date with the highest temperature was {df["Date"].iloc[lowestTempIndex]} at {df["Temperature (C)"].iloc[lowestTempIndex]} degrees celsius")

# Create graphs that show the trends and patterns over time for both the temperature and precipitation
def GraphsForTrendsAndPatternsOverTime():
    df = pd.read_csv("WeatherData.csv")

    plt.plot(df["Date"],df["Temperature (C)"], label="Temperature (C)")
    plt.title("Temperature over Time")
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# Analyse trends and patters over time for both units and sold and revenue
def NintendoUnitsSoldAndRevenue():
    df = pd.read_csv("nintendo_game_sales.csv")

    while True:
        try:
            graphChoice = input("1) Two graphs \n2) Twin axes\n")
            df["ReleaseYear"] = df["ReleaseYear"].astype(int)
            df_sortedByYear = df.sort_values(by="ReleaseYear")
        
            if graphChoice == "1":
                

                fig, axes = plt.subplots(2, 1)
                axes[0].plot(df_sortedByYear["ReleaseYear"], df_sortedByYear["UnitsSold_Millions"])
                axes[1].plot(df_sortedByYear["ReleaseYear"], df_sortedByYear["Revenue_USD_Millions"])
                plt.show()
                break

            elif graphChoice == "2":
                fig, ax1 = plt.subplots()

                ax1.plot(df_sortedByYear["ReleaseYear"], df_sortedByYear["UnitsSold_Millions"])

                ax2 = ax1.twinx()
                ax2.plot(df_sortedByYear["ReleaseYear"], df_sortedByYear["Revenue_USD_Millions"])
                plt.show()
                break
            
            else:
                print("Invalid choice")
        except:
            print("Error")
    
# Find the games that made the most revenue and sold the most units, as well as the lowest
def NintendoMostAndLeastUnitsSoldAndRevenue():
    return 0

# Create a bar chart to show the sales of specifically the Pokémon games
def PokemonGameSalesGraph():
    return 0


while True:
    choice = input("Select an option: ")

    if choice == "1":
        CalculateAverageTempAndPrec()
    elif choice == "2":
        LowestAndHighestValues()
    elif choice == "3":
        GraphsForTrendsAndPatternsOverTime()
    elif choice == "4":
        NintendoUnitsSoldAndRevenue()
    elif choice == "5":
        NintendoMostAndLeastUnitsSoldAndRevenue()
    elif choice == "6":
        PokemonGameSalesGraph()



