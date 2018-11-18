#!/usr/bin/env python
import json

import matplotlib.pyplot as plt
import numpy as np

# Data
# ... Raw data
prices = []
ratings = []
price_rating = []

with open('specs.json', 'r') as f:
    for i in json.load(f):
        if i['price'] < 0:
            continue

        prices.append(i['price'])
        ratings.append(i['rating'])
        price_rating.append([i['price'], i['rating']])

# ... Binned
price_bins = np.array([float(i*100) for i in range(40)])
price_bin_indexes = np.digitize(np.array(prices), price_bins)

binned_prices = []
binned_ratings = []
binned_price_rating = []

binned_summed_ratings = []
binned_summed_ratings_count = []
for i in range(len(price_bins)):
    binned_summed_ratings.append(0)
    binned_summed_ratings_count.append(0)

for i, bin_i in enumerate(price_bin_indexes):
    price = price_bins[bin_i-1]
    rating = price_rating[i][1]

    binned_price_rating.append([price, rating])
    binned_prices.append(price)
    binned_ratings.append(rating)
    binned_summed_ratings[bin_i-1] += rating
    binned_summed_ratings_count[bin_i-1] += 1

binned_avrg_ratings = []
for i, summed_ratings in enumerate(binned_summed_ratings):
    if binned_summed_ratings_count[i] == 0:
        binned_avrg_ratings.append(0)
    else:
        binned_avrg_ratings.append(summed_ratings / binned_summed_ratings_count[i])

print("Correlation: {}".format(np.correlate(prices, ratings)))

# Plot
fig, ax = plt.subplots()

ax.set_xlabel("Price")
ax.set_ylabel("Rating")

ax.scatter(binned_prices, binned_ratings, label='Binned Price vs Rating', color='blue')
ax.plot(price_bins, binned_avrg_ratings, label='Average Binned Price vs Rating', color='red')

fig.legend()
plt.show()
