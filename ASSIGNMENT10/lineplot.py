import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, linestyle="--", marker="o", color="red")

plt.title("Customized Line Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()