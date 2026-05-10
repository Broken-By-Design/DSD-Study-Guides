import pandas as pd
import matplotlib.pyplot as plt


"""
# Bar Chart Practice

df = pd.read_csv("theme_park_rides.csv")

#print(df.to_string(index = False))

averageWaitTimes = round(df.groupby("ride_name")["wait_time_minutes"].mean(), 2)

df2 = averageWaitTimes.reset_index()

print(df2.to_string(index=False))

plt.bar(df2["ride_name"], df2["wait_time_minutes"])
plt.title("Average Wait Time for each Ride")
plt.xlabel("Ride")
plt.ylabel("Wait Time")
plt.grid()
plt.show()


medianWaitTimes = df.groupby("category")["wait_time_minutes"].median()

df3 = medianWaitTimes.reset_index()

plt.bar(df3["category"], df3["wait_time_minutes"], color=["orange", "green", "blue"])
plt.title("Median Wait Time for each Ride")
plt.xlabel("Ride Category")
plt.ylabel("Wait Time")
plt.grid()
plt.show()
"""

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


areas = df["area"].unique()

timesToPlot = []
for time in df["time"]:
    timesToPlot.append(str(time))
bigLine = plt.plot(timesToPlot, df["number_of_people_visited"], label="All")

for area in areas:
    lineToPlot = df[df["area"] == area]
    print(lineToPlot)
    timesToPlot = []
    for time in lineToPlot["time"]:
        timesToPlot.append(str(time))
    plt.plot(timesToPlot, lineToPlot["number_of_people_visited"], label=area)


l = bigLine.pop(0)
l.remove()

plt.xticks(rotation=90)
plt.legend()
plt.show()

