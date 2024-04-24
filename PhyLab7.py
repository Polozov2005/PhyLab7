import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import locale

# Количество строк
row = 20

# Количество столбцов
column = 3

# Объявление таблицы
A = np.zeros((row + 1, column + 1))
for i in range(1, row + 1):
    A[i, 0] = i
for j in range(1, column + 1):
    A[0, j] = j

# 1. Напряжение, показываемое вольтметром, 10^(-3) В
A[1:row + 1, 1:1 + 1] = [
    [925],
    [875],
    [825],
    [775],
    [725],
    [675],
    [625],
    [575],
    [525],
    [475],
    [425],
    [375],
    [325],
    [275],
    [225],
    [175],
    [125],
    [75],
    [25],
    [2]
]
A[1:row + 1, 1:1 + 1] = - A[1:row + 1, 1:1 + 1]

# 2. Анодный ток, 10^-6 А
A[1:row + 1, 2:2 + 1] = [
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [10],
    [12],
    [18],
    [31],
    [51],
    [83],
    [133],
    [215],
    [353],
    [595],
    [977],
    [1545],
    [1943]
]

# 3. Что-то, в чём-то
# A[1:row + 1, 3:3 + 1] = np.log(A[1:row + 1, 2:2 + 1] / A[row, 2])
# A[1:row + 1, 3:3 + 1] = np.log(A[1:row + 1, 2:2 + 1] / A[1, 2])
A[1:row + 1, 3:3 + 1] = np.log(A[1:row + 1, 2:2 + 1])

# Вывод таблицы
df_A = pd.DataFrame(A)
df_A = df_A.drop(index=[0])
df_A = df_A.drop(columns=[0])
rounded_df_A = df_A.round(decimals=1)
print(rounded_df_A)

# x = A[1:row + 1, 1:1 + 1]
# y = A[1:row + 1, 2:2 + 1]
# plt.plot(x, y)

# plt.show()


x = A[1:row + 1, 1:1 + 1]
y = A[1:row + 1, 3:3 + 1]
plt.plot(x, y)

plt.show()