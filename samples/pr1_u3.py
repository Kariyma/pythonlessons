import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-100, 100.01, 0.01)


def foo_y(x=1):
    a = 1 + np.tan(1 / (1 + np.sin(x) ** 2))
    b = (x ** 2 + 1) * np.exp(-(np.abs(x) / 10))
    y = np.log(b)/np.log(a)
    return y


plt.plot(t, foo_y(t), 'g')
plt.grid(True)

plt.show()
