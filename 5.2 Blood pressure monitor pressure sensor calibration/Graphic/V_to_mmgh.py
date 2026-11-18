import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

folder = '..'
files = ['40_1.csv', '40_2.csv', '40_3.csv', '80_1.csv', '120.csv', '160.csv']

plt.figure(figsize=(14, 8))

for file in files:
    filepath = os.path.join(folder, file)

    if not os.path.exists(filepath):
        continue

    try:
        df = pd.read_csv(filepath)
        time_raw = df.iloc[:, 0].values
        voltage_raw = df.iloc[:, 1].values


        mask = (time_raw >= 2) & (time_raw <= 6)
        time_filtered = time_raw[mask]
        voltage_filtered = voltage_raw[mask]

        t_min = time_filtered.min()
        t_max = time_filtered.max()



        time_stretched = (time_filtered - t_min) / (t_max - t_min) * 10

        mean_v = voltage_filtered.mean()


        print(f"{file:10} | Среднее: {mean_v:.4f} В")


        plt.plot(time_stretched, voltage_filtered, label=f'{file} (ср: {mean_v:.3f})', alpha=0.8)
        plt.axhline(y=mean_v, linestyle=':', alpha=0.4)

    except Exception as e:
        print(f"Ошибка с {file}: {e}")

# Жестко задаем ось X от 0 до 10
plt.xlim(0, 10)

plt.title('График зависимости U(t)')
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('plot.png')
plt.show()