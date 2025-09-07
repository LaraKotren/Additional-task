import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01, 10, 0.01)

y = np.log(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='ln(x)', color='blue')

plt.title('График натурального логарифма')
plt.xlabel('x')
plt.ylabel('ln(x)')
plt.grid(True)
plt.legend()

plt.show()
