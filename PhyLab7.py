import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd
import locale

# Количество строк
row = 20

# Количество столбцов
column = 5

# Объявление таблицы
A = np.zeros((row + 1, column + 1))

# 1. Напряжение между анодом и катодом, мВ
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

# 2. Анодный ток, мкА
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

# 3. Натуральный логарифм анодного тока, ln(мкА)
A[1:row + 1, 3:3 + 1] = np.log(A[1:row + 1, 2:2 + 1])

# 4. Погрешность измерения напряжения между анодом и катодом, мВ
A[1:row + 1, 4:4 + 1] = 1

# 5. Погрешность измерения натурального логарифма анодного тока, ln(мкА)
A[1:row + 1, 5:5 + 1] = np.mean(A[1:row + 1, 3:3 + 1]) * A[1:row + 1, 4:4 + 1] / np.mean(A[1:row + 1, 1:1 + 1])

# Вывод таблицы
df_A = pd.DataFrame(A)
df_A = df_A.drop(index=[0])
df_A = df_A.drop(columns=[0])
rounded_df_A = df_A.round(decimals=2)
print(rounded_df_A)

# Настройки графика
fig, ax = plt.subplots()
locale.setlocale(locale.LC_NUMERIC, "de_RU")
font = {'family': 'Times New Roman',
        'size': 12}
plt.rc('font', **font)
ax.ticklabel_format(useLocale=True)
ax.grid(linewidth = 0.3)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()

ax.plot(A[1:row + 1, 1:1 + 1], A[1:row + 1, 3:3 + 1], color='black')
plt.ylim(0)

plt.savefig('graph.pdf')
plt.show()