import numpy as np
import pandas as pd
from scipy.signal import find_peaks

import matplotlib.pyplot as plt

data = pd.read_csv("/home/sercan/Desktop/project/data/data.csv")
data2 = pd.read_csv("data/prngsize(byte).csv")  # Reading data
data3 = pd.read_csv("data/idle.csv")

name = data2.name
size = data2.Size
x = data.Current
current = data.Current
voltage = data.Voltage
time = data.Time

peaks, _ = find_peaks(x, height=0.9)  # finding peaks

first, last = int, int

for i in range(len(current)):
    if current[i] > 0.9:
        first = i
        break

        # finding when it starts when it ends
for i in reversed(range(len(current))):
    if current[i] > 0.9:
        last = i
        break

starter_peak = [first]
ending_peak = []

for i in range(len(peaks)):
    if peaks[i] - peaks[i - 1] > 15:
        starter_peak.append(peaks[i])  # finding when first spike when last spike of a prng
        ending_peak.append(peaks[i - 1])

ending_peak.append(last)
power = []
energy = []
delta_time = []
avg_current = []
avg_voltage = []

c_list = []
n1 = []
v_list = []
n2 = []
t_list = []
n3 = []

avg_idle = (np.mean(data3.Current)) * 5

for i in range(len(starter_peak)):
    for j in range(len(current[starter_peak[i]:ending_peak[i]])):  # 2d list of prng current and voltage values
        n1.append(current[starter_peak[i] + j])
        n2.append(voltage[starter_peak[i] + j])
        n3.append(time[starter_peak[i] + j])
    c_list.append(n1)
    v_list.append(n2)
    t_list.append(n3)
    n1 = []
    n2 = []
    n3 = []

n4, ins_power = [], []
mean_current = 0
for i in range(len(starter_peak)):
    for j in range(0, len(c_list[i]), 1):
        mean_current = np.mean((c_list[i][j:j + 2]))
        n4.append(mean_current)

    ins_power.append(n4)
    n4 = []

itersize = []
energy_per_bits = []
iterations = []
for i in range(len(starter_peak)):
    if size[i] == 4:
        iter_size = (150000000 * 32)
        t = len(t_list[i])
        itersize.append(iter_size)
    else:
        iter_size = (150000000 * 64)
        t = len(t_list[i])
        itersize.append(iter_size)
    avg_current.append(np.mean(current[starter_peak[i]:ending_peak[i]]))
    avg_voltage.append(np.mean(voltage[starter_peak[i]:ending_peak[i]]))  # calculating expected values
    power.append((avg_current[i] * avg_voltage[i]) - avg_idle)
    delta_time.append((ending_peak[i] - starter_peak[i]) / 10)
    energy.append(power[i] * delta_time[i])
    energy_per_bits.append(energy[i] / itersize[i])
    iterations.append((energy[i] / 150000000))

fig = plt.figure()
plt.plot(x, markevery=(starter_peak + ending_peak), marker='*', mec='red')  # testing spikes.
plt.xticks(ending_peak)
fig.set_size_inches(200, 2)
plt.show()

calc_data = []
header = ['Name', 'Power', 'Delta Time', 'Energy', 'EnergyperBits', 'EnergyperIteration']

for i in range(len(starter_peak)):
    calc_data.append([name[i], power[i], delta_time[i], energy[i], energy_per_bits[i], iterations[i]])  # creating csv

calc_data = pd.DataFrame(calc_data, columns=header)
calc_data.to_csv('data/calc_data.csv', index=False)
