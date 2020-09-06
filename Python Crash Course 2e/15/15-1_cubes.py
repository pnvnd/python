import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

x_values = range(1, 5001)
square_values = [x**2 for x in x_values]
cube_values = [x**3 for x in x_values]

plt.style.use("dark_background")
fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
# ax.scatter(input_values, squares, s=600)

# ax.plot(x_values, square_values, linewidth=1)
# ax.plot(x_values, cube_values, linewidth=1)
ax.scatter(x_values, square_values, s=1, c=square_values, cmap=plt.cm.Reds)
ax.scatter(x_values, cube_values, s=1, c=cube_values, cmap=plt.cm.Blues)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", labelsize=14)

# Set the range for each axis.
# ax.axis([0,1100, 0, 1100000])

plt.savefig("cubes_plot.png", bbox_inches="tight")
plt.show()
