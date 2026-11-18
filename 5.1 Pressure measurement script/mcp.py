import time
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time
from adc_gist import plot_sampling_period_hist

import RPi.GPIO as g

g.setmode(g.BCM)

led = 14

g.setup(led, g.OUT)

voltage_values = []
time_values = []
duration = 60.0

adc = None

try:
    adc = MCP3021(dynamic_range=5.0)

    g.output(led, 1)
    time.sleep(30)
    print("charged")
    g.output(led, 0)

    start_time = time.time()

    while time.time() - start_time < duration:
        voltage = adc.get_voltage()
        voltage_values.append(voltage)
        time_values.append(time.time() - start_time)

    plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
    #plot_sampling_period_hist(time_values)

finally:
    if adc is not None:
        adc.deinit()