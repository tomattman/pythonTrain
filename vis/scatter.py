import matplotlib.pyplot as plt

x_values = list(range(1 , 101))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, s = 40, edgecolor='none')
plt.axis([0, 100, 0, 10000])

plt.savefig("squares.png", bbox_inches='tight')