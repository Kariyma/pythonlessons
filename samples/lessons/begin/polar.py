import numpy as np
import matplotlib.pyplot as plt

a = 1
angle = np.arange(0, 100.1, 0.1)

plt.polar(angle, (a / (2*np.pi))*angle)
plt.show()

