import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV, makes the dataframe indexed at 0
df = pd.read_csv("theme_park_ticket_sales.csv", index_col=0)

# Transpose so rows = dates, columns = ticket types
df_t = df.T

# Convert index to datetime for proper plotting on x-axis
df_t.index = pd.to_datetime(df_t.index)

# Plot
plt.figure(figsize=(14, 7))

# Plots a line for each column, using the index (date) as the x-axis
for ticket_type in df_t.columns:
    plt.plot(df_t.index, df_t[ticket_type], label=ticket_type)

plt.xlabel("Date")
plt.ylabel("Tickets Sold")
plt.title("Theme Park Ticket Sales Over Time")
plt.legend(title="Ticket Type", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
