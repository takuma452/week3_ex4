import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib

def true_function(x):
  """
  >>> true_function(0)
0.0
  """
  return np.sin(np.pi * x * 0.8) * 10
# 乱数のシード値を設定
np.random.seed(0)

# 乱数の個数
n = 20

x_obs = np.random.uniform(-1, 1, n)
y_true = true_function(x_obs)


df = pd.DataFrame({
    '観測点': x_obs,
    '真値': y_true
})
# 確認
print(df)

x = np.linspace(-1, 1, 100)
y = true_function(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y , label='y = 10 * sin(0.8 * pi * x)', color='blue')

# 観測点をプロット
plt.scatter(df['観測点'], df['真値'], color='red', label='観測点', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('真値と観測点のプロット')
plt.grid(True)
plt.legend()

# 画像として保存
plt.savefig('ex1.2.png')
plt.show()