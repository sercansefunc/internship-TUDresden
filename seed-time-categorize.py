import pandas as pd

data = pd.read_csv("data/time.csv")

name = data.name
time = data.time

short, mid, long = [], [], []
for i in range(len(time)):
    if time[i] < 1000:
        short.append([name[i], time[i]])
    elif time[i] < 13000:
        mid.append([name[i], data.time[i]])
    else:
        long.append([name[i], time[i]])

header = ['name', 'time']
df1 = pd.DataFrame(short, columns=header)
df1.to_csv('data/short.csv', index=False)

df2 = pd.DataFrame(mid, columns=header)
df2.to_csv('data/mid.csv', index=False)

df3 = pd.DataFrame(long, columns=header)
df3.to_csv('data/long.csv', index=False)
