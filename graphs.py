import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/calc_data_seed.csv")
energy_per_bits = df.energyperseed
sorted_df = df.sort_values(by="energyperseed", ascending=False)
fig = plt.figure()
"""plt.bar(sorted_df.name,sorted_df.energyperseed)
plt.xticks(rotation=90)
plt.ylabel('Energy / Seed')
plt.margins(x=0.01,y=0.01)
plt.title('Energy per Seed for each PRNG')
plt.yscale("log")
plt.tight_layout()
plt.savefig('graphs/energy_per_seed.png')
plt.show()"""

"""df=pd.read_csv("data/script.log")
throughput=df.Mbps
sorted_df=df.sort_values(by="Mbps",ascending=False)

plt.bar(sorted_df.name,sorted_df.Mbps)
plt.xticks(rotation=90)
plt.ylabel('Throughput [Mbps]')
plt.xlabel('PRNG Algorithm')
plt.margins(x=0.01,y=0.01)
plt.yscale("log")
plt.tight_layout()
#plt.savefig('graphs/throughput.png')
plt.show()"""

"""df=pd.read_csv("data/calc_data.csv")
energy_per_bits=df.EnergyperBits
sorted_df=df.sort_values(by="EnergyperBits",ascending=False)
fig=plt.figure()

plt.bar(sorted_df.Name,sorted_df.EnergyperBits)
plt.xticks(rotation=90)
plt.ylabel('Joules / Bits')
plt.margins(x=0.01,y=0.01)
plt.title('Energy per bits for each PRNG')
plt.yscale("log")
plt.tight_layout()
plt.savefig('graphs/energy_per_bits.png')
plt.show()"""

"""sorted_df2=df.sort_values(by="EnergyperIteration",ascending=False)

plt.bar(sorted_df2.Name,sorted_df2.EnergyperIteration)
plt.xticks(rotation=90)
plt.ylabel('Joules / #iteration')
plt.margins(x=0.01,y=0.01)
plt.title('Energy per iteration for each PRNG')
plt.yscale("log")
plt.tight_layout()
plt.savefig('graphs/energy_per_iter.png')
plt.show()"""
