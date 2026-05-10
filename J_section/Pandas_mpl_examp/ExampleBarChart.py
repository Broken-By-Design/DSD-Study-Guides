import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

plt.bar(categories, values)
plt.title("Bar Chart Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
