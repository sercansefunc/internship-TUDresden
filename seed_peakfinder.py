import pandas as pd
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv("data/short_data_500000000.csv")
data2 = pd.read_csv("data/short.csv")
data3 = pd.read_csv("data/idle.csv")
data4 = pd.read_csv("data/mid_data_1000000.csv")
data5 = pd.read_csv("data/long_data_5000.csv")
data7 = pd.read_csv("data/long.csv")
data6 = pd.read_csv("data/mid.csv")

mid_n = data6.name
long_n = data7.name
short_n = data2.name

seed_mid_c = data4.Current
seed_long_c = data5.Current
seed_short_c = data1.Current

peaks_short, _ = find_peaks(seed_short_c, height=0.9)
peaks_mid, _ = find_peaks(seed_mid_c, height=0.9)
peaks_long, _ = find_peaks(seed_long_c, height=0.9)

avg_idle = (np.mean(data3.Current)) * 5

for i in range(len(seed_short_c)):
    if seed_short_c[i] > 0.9:
        first_short = i
        break
        # finding when it starts when it ends
for i in reversed(range(len(seed_mid_c))):
    if seed_mid_c[i] > 0.9:
        last_short = i
        break

for i in range(len(seed_mid_c)):
    if seed_mid_c[i] > 0.9:
        first_mid = i
        break
        # finding when it starts when it ends
for i in reversed(range(len(seed_mid_c))):
    if seed_mid_c[i] > 0.9:
        last_mid = i
        break

for i in range(len(seed_long_c)):
    if seed_long_c[i] > 0.9:
        first_long = i
        break

        # finding when it starts when it ends
for i in reversed(range(len(seed_long_c))):
    if seed_long_c[i] > 0.9:
        last_long = i
        break

short_starter = [first_short]
short_ending = []
long_starter = [first_long]
mid_starter = [first_mid]
long_ending = []
mid_ending = []

for i in range(len(peaks_short)):
    if peaks_short[i] - peaks_short[i - 1] > 15:
        short_starter.append(peaks_short[i])  # finding when first spike when last spike of a prng
        short_ending.append(peaks_short[i - 1])

for i in range(len(peaks_mid)):
    if peaks_mid[i] - peaks_mid[i - 1] > 15:
        mid_starter.append(peaks_mid[i])  # finding when first spike when last spike of a prng
        mid_ending.append(peaks_mid[i - 1])

for i in range(len(peaks_long)):
    if peaks_long[i] - peaks_long[i - 1] > 15:
        long_starter.append(peaks_long[i])  # finding when first spike when last spike of a prng
        long_ending.append(peaks_long[i - 1])

mid_ending.append(last_mid)
long_ending.append(last_long)
short_ending.append(last_short)

fig = plt.figure()
plt.plot(seed_short_c, markevery=(short_starter + short_ending), marker='*', mec='red')  # testing spikes.
plt.xticks(short_ending)
fig.set_size_inches(200, 2)
plt.show()

power_mid = []
delta_time_mid = []
energy_mid = []
energy_per_seed_mid = []
mid_avg_c = []
for i in range(len(mid_starter)):
    mid_avg_c.append(np.mean(seed_mid_c[mid_starter[i]:mid_ending[i]]))
    power_mid.append(5 * mid_avg_c[i] - avg_idle)
    delta_time_mid.append((mid_ending[i] - mid_starter[i]) / 10)
    energy_mid.append(power_mid[i] * delta_time_mid[i])
    energy_per_seed_mid.append(energy_mid[i] / 1000000)

long_avg_c, power_long, delta_time_long, energy_long, energy_per_seed_long = [], [], [], [], []
for i in range(len(long_starter)):
    long_avg_c.append(np.mean(seed_long_c[long_starter[i]:long_ending[i]]))
    power_long.append((5 * long_avg_c[i]) - avg_idle)
    delta_time_long.append((long_ending[i] - long_starter[i]) / 10)
    energy_long.append(power_long[i] * delta_time_long[i])
    energy_per_seed_long.append(energy_long[i] / 5000)

power_short = []
delta_time_short = []
energy_short = []
energy_per_seed_short = []
short_avg_c = []
for i in range(len(short_starter)):
    short_avg_c.append(np.mean(seed_short_c[short_starter[i]:short_ending[i]]))
    power_short.append(5 * short_avg_c[i] - avg_idle)
    delta_time_short.append((short_ending[i] - short_starter[i]) / 10)
    energy_short.append(power_short[i] * delta_time_short[i])
    energy_per_seed_short.append(energy_short[i] / 500000000)

calc_data_mid = []
for i in range(len(mid_starter)):
    calc_data_mid.append([mid_n[i], energy_per_seed_mid[i]])

calc_data_long = []
for i in range(len(long_starter)):
    calc_data_mid.append([long_n[i], energy_per_seed_long[i]])

for i in range(len(short_starter)):
    calc_data_mid.append([short_n[i], energy_per_seed_short[i]])

header_mid = ['name', 'energyperseed']
calc_data_mid = pd.DataFrame(calc_data_mid, columns=header_mid)
calc_data_mid.to_csv('data/calc_data_seed.csv', index=False)
