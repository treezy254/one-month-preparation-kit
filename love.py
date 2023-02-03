import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 5, 10000)

y = x**2/3 - np.sqrt(3.3 - (x**2 * np.sin(6 * np.pi * x)))

print(y)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y, 'b')
plt.show()
