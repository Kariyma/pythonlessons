import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-50, 50.01, 0.01)

foo_name = input('ваша функция? ')
print('вы ввели', foo_name)

with plt.xkcd():
    plt.plot(x, eval(foo_name))
    plt.grid(True)

plt.show()
