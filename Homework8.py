print ("EXERCISE 9.1")
print("The graph will shortly appear in a new window")

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), color='red', linestyle='solid', label='sin(x)')
plt.plot(x, np.cos(x), color='green', linestyle='dashed', label='cos(x)')
plt.plot(x, np.exp(-x), color='blue', linestyle='dotted', label='exp(-x)')

plt.legend()

plt.show()

print ("EXERCISE 9.2")
print("The graph will shortly appear in a new window")

n = 100
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

dist = np.sqrt(x**2 + y**2)

area = np.abs(x) + np.abs(y)
colors = np.where(dist < 1, 'green', 'red')
plt.scatter(x, y, s=100*area, c=colors)

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.show()

