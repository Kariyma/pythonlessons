import numpy as np
import matplotlib.pyplot as plt

data = [33, 25, 20, 12, 10]
plt.figure(num=1, figsize=(10, 10))
plt.axes(aspect=1)
plt.title('Plot 3', size=14)
explode = (0.05, 0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
plt.pie(data, explode=explode, labels=('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'), autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.show()
