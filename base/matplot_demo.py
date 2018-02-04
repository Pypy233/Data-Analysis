import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x + 1) + 1

plt.figure(figsize=(8, 4))

plt.plot(x, y, label = '$\sinx + 1$', color = 'red')

plt.plot(x, z, 'b--', label = '$\cosx^2 + 1$')

plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('A Simple Demo')
plt.ylim(0, 2)
plt.legend()
plt.savefig('out/demo.png')
plt.show()