import numpy as np
import matplotlib.pyplot as plt

def true_function(x):
  """
  >>> true_function(0)
0.0
  """
  return np.sin(np.pi * x * 0.8) * 10

x = np.linspace(-1, 1, 100)
y = true_function(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y , label='y = 10 * sin(0.8 * pi * x)', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('true_function')
plt.legend()

# 画像として保存
plt.savefig('week3/ex4/ex1.1.png')
plt.show()