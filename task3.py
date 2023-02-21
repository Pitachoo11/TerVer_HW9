import numpy as np

# Входные данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Настройки алгоритма
alpha = 1e-6
n_iterations = 100000

# Инициализация коэффициентов
w = 0
b = 0

# Градиентный спуск
n = len(zp)
for i in range(n_iterations):
    y_pred = w * zp + b
    error = y_pred - ks
    w -= alpha * (2/n) * np.sum(error * zp)
    b -= alpha * (2/n) * np.sum(error)

print("Коэффициенты линейной регрессии:")
print(f"w = {w}, b = {b}")
print(f'Уравнение линейной регрессии для данных входных значений будет иметь вид:')
print(f'y = {w:.2f}x + {b:.2f}')