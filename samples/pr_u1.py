import numpy as np
# x = np.arange(-10, 10.01, 0.01)
x = [1, 10, 1000]

# a = 1 + x**2
# b = (1/(np.e**np.sin(x) + 1))/(5/4 + 1/(x**15))
for i in x:
    y = np.log((1/(np.e**np.sin(i) + 1))/(5/4 + 1/(i**15)))/np.log(1 + i**2)
    print('x', i)
    print('y', y)
