import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [4, 5, 6]

x2 = [1, 3, 5]
y2 = [10, 11, 12]

# Draws a bar chart, takes x and y values as parameters
plt.bar(x, y)

# Gives the graph a title, takes a string as a parameter for the title
plt.title("Giraffe")

# Labels the x-axis, takes a string as a parameter for the label
plt.xlabel("Name")

# Labels the y-axis, takes a string as a parameter for the label
plt.ylabel("Length of Neck")

# Draws a grid on the background to make it easier to read
plt.grid()

# Shows the final graph(s), does not output a graph without this function, takes the results of the previous functions for the output
plt.show()

# Plots a line for a line chart, takes x and y values as parameters, add in a label parameter to set up a legend
plt.plot(x, y, label = "crack")

# Plotting a second line with a different colour and marker
plt.plot(x2, y2, color = "pink", marker = 'x', label = "meth")

# Creates a key so the user can see what line represents what
plt.legend()


plt.title("Drug usage in Harlow")
plt.xlabel("Sales per day")
plt.ylabel("Visits to Princess Alexandra Hospital")
plt.grid()
plt.show()
