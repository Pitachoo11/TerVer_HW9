import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# средние значения
mean_x = np.mean(zp)
mean_y = np.mean(ks)

# произведения их соответствующих элементов
xy = np.mean(zp * ks)

# средние значения квадратов x
x2 = np.mean(zp ** 2)

# Расчет коэффициентов линейной регрессии с интерцептом
# коэффициент наклона 1
b_with_intercept = (xy - mean_x * mean_y) / (x2 - mean_x ** 2)

# свободный член
a_with_intercept = mean_y - b_with_intercept * mean_x

print("Коэффициент наклона с intercept:", b_with_intercept)
print("Свободный член с intercept:", a_with_intercept)

# Расчет коэффициентов линейной регрессии без интерцепта
# коэффициент наклона
b_without_intercept = xy / x2

print("Коэффициент наклона без intercept:", b_without_intercept)