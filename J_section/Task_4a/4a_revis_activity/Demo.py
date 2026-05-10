import pandas as pd

import matplotlib.pyplot as plt # Graphs library

df = pd.read_csv("GreenLeaf_Classroom_Example.csv")

# Group By - Splits data into groups based on the selected column(s), then you can apply calculations on each group

groupedObject = df.groupby(["Post Category"])

sumGroupBy = groupedObject["Likes"].sum() # maths function to total groups together

meanGroupBy = groupedObject["Likes"].mean() # mean function to get averages of groups

df2 = sumGroupBy.reset_index()

print(df)


# Turning the grouped data into a graph

plt.bar(df2["Post Category"], df2["Likes"])
plt.show()

# Index functions

print(df["Likes"].idxmax())
print(df["Likes"].idxmin())

LowestLikesRowIndex = df["Likes"].idxmin()

# iloc() - Locates using the index of a row
WorstDate = df["Date"].iloc[LowestLikesRowIndex]

print(f"The date with the worst performing post was {WorstDate}")

