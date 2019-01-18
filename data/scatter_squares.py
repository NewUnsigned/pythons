import matplotlib.pyplot as plt

for i in range(1, 10):
    plt.scatter(2*i, 4*i, s=200)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

