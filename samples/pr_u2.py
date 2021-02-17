import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2.5, 3.5, 0.01)

plt.plot(x, x*x - x - 6)
plt.title(r'$x*x - x - 6$')
plt.grid(True)

# y(x) = x*x - x - 6

plt.show()
