import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("theme_park_ticket_sales.csv", index_col = 0)

df_t = df.T

print(df_t["VIP"].idxmax())
