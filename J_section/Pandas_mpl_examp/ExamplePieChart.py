import matplotlib.pyplot as plt

labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [30, 25, 20, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()
