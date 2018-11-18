#!/usr/bin/env python
import json

import matplotlib.pyplot as plt
import numpy as np

# Data
x = []
raw_data = []

with open('specs.json', 'r') as f:
    for i in json.load(f):
        if i['price'] < 0:
            continue

        x.append(i['price'])
        raw_data.append([i['price'], i['rating']])

x = np.array(x)

price_bins = np.array([float(i*100) for i in range(40)])
bin_indexes = np.digitize(x, price_bins)

bined_data_x = []
bined_data_y = []
for i, bin_i in enumerate(bin_indexes):
    bined_data_x.append(price_bins[bin_i-1])
    bined_data_y.append(raw_data[i][1])

z = np.polyfit(bined_data_x, bined_data_y, 1)
p = np.poly1d(z)

# Plot
fig, ax = plt.subplots()

ax.set_xlabel("Price")
ax.set_ylabel("Rating")

ax.scatter(bined_data_x, bined_data_y, label='Price vs Rating')

ax.plot(bined_data_x, p(bined_data_x), label='Fit', color='orange')

fig.legend()
plt.show()
