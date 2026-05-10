import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("theme_park_times_with_visitors.csv")

# Convert timestamp column to datetime
df["visit_timestamp"] = pd.to_datetime(df["visit_timestamp"])

# Split into date and time columns
df["date"] = df["visit_timestamp"].dt.date
df["time"] = df["visit_timestamp"].dt.time

# Sort by timestamp for proper plotting
df = df.sort_values("visit_timestamp")

# Plot: number of people visited over time for each area
plt.figure(figsize=(12, 6))

areas = df["area"].unique()

for area in areas:
    subset = df[df["area"] == area]
    plt.plot(subset["visit_timestamp"], subset["number_of_people_visited"], label=area)

plt.xlabel("Time")
plt.ylabel("Number of People Visited")
plt.title("Visitors Over Time by Theme Park Area")
plt.legend(title="Area")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
