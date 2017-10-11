import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.scatter(input_values, squares)

#plt.plot(input_values, squares, linewidth = 5)
plt.title("Square numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)
plt.tick_params(axis = 'both', labelsize = 14)
plt.show()