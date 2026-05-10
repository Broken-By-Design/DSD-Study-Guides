import pandas as pd
import matplotlib.pyplot as plt

# Line Chart Practice

df = pd.read_csv("theme_park_times.csv")

#print(df.to_string(index=False))

# Convert data passed into function to datetime (usually from a string)
df["visit_timestamp"] = pd.to_datetime(df["visit_timestamp"])

# Creates two new columns, called date and time, and stores the datetime data separately
df["date"] = df["visit_timestamp"].dt.date
df["time"] = df["visit_timestamp"].dt.time

# Built-in function to order values so the graph doesn't plot incorrectly
df = df.sort_values("visit_timestamp")

# Puts all the unique values in the area column into a list
areas = df["area"].unique()

# Create a list for the time values for the x-axis converted to string data
timesToPlot = []

# Look through the time column, converting the time data to string data and appending it to the list
for time in df["time"]:
    timesToPlot.append(str(time))

# Plots a big line so that all of the ordered data gets displayed, preparing to
# insert smaller data across all plotted points
bigLine = plt.plot(timesToPlot, df["number_of_people_visited"], label="All")

# Creates smaller dataframes for each area so that the individual lines are plotted
#  for each one
for area in areas:
    lineToPlot = df[df["area"] == area]
    #print(lineToPlot)
    timesToPlot = []
    for time in lineToPlot["time"]:
        timesToPlot.append(str(time))
    plt.plot(timesToPlot, lineToPlot["number_of_people_visited"], label=area)


l = bigLine.pop(0) # Creates a variable to remove the big line, because we don't want to see it
l.remove() # Removes the big line from the graph

plt.xticks(rotation=90)
plt.show()

