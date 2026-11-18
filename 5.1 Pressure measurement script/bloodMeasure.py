import time
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time
import numpy as np

voltage_values = []
time_values = []
duration = 60.0

adc = None

try:
    adc = MCP3021(dynamic_range=5.0)

    start_time = time.time()

    while time.time() - start_time < duration:
        voltage = adc.get_voltage()
        voltage_values.append(voltage*80/0.92 -13)
        time_values.append(time.time() - start_time)

    plot_voltage_vs_time(time_values, voltage_values, 250)
    #plot_sampling_period_hist(time_values)


finally:
    if adc is not None:
        adc.deinit()


data = np.column_stack((time_values, voltage_values))

np.savetxt('fitness_Mas.csv',
           data, delimiter=',',
           fmt='%.4f',
           header='Время[c],Давление[мм рт.ст.]',
           comments='',
           encoding='utf-8')