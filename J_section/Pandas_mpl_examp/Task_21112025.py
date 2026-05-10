"""
-Find the date with the highest total sales and create a report which breaks down all the ticket sales for that day
-Create a bar chart that shows total sales for each ticket type
-Create a line chart that shows sales for each type of ticket over time, INCLUDING the total sales
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("theme_park_ticket_sales.csv", index_col=0)

df_t = df.T

df_t["Total Sales"] = df_t["Adult"] + df_t["Child"] + df_t["Senior"] + df_t["VIP"] + df_t["FastPass"] + df_t["Group Package"] + df_t["Season Pass"]

highestSalesDay = df_t["Total Sales"].idxmax()
highestSalesData = df_t.loc[highestSalesDay]

print(f"The day with the highest sales was {highestSalesDay}")
print(f"Adult Tickets: {highestSalesData["Adult"]}")
print(f"Total Sales: {highestSalesData["Total Sales"]}")


totalSalesForTypes = [
    df_t["Adult"].sum(),
    df_t["Child"].sum(),
    df_t["Senior"].sum(),
    df_t["VIP"].sum(),
    df_t["FastPass"].sum(),
    df_t["Group Package"].sum(),
    df_t["Season Pass"].sum()
    ]

plt.bar(df.index, totalSalesForTypes)
plt.xlabel("Ticket Type")
plt.ylabel("Sales")
plt.title("Total Sales per Ticket Type")
plt.show()
