import matplotlib.pyplot as plt
import numpy as np
x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.5, 1.5, 1])
A = np.vstack([x, np.ones(len(x))]).T
plt.plot(x, y, 'o', markersize=10)
a = np.array([[1, 2],[3, 4]])
b = np.array([[1, 2],[1,3]])
plt.plot(x, a*x + b, 'r' , linewidth=3)
plt.xlim( 6.1,3.1)
plt.ylim( 1.1,2.6)
plt.grid(True)
plt.show()