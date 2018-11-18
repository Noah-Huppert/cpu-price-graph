#!/usr/bin/env python3
# Places cpubenchmark.net results in csv file
# Columns: cpu, rating, price
import csv
import argparse

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import requests

URL = 'https://www.cpubenchmark.net/high_end_cpus.html'

# Make request
raw_resp = requests.get(URL)

# Parse
resp = HtmlResponse(body=raw_resp.text)
s = Selector(response=resp)

cpus = []

for row in s.xpath('/html/body/center/div[5]/div[2]/table/tbody').xpath('tr'):
    cpus.append({
        'cpu': row.xpath('td[0]/text()').extract(),
        'rating': row.xpath('td[1]/text()').extract(),
        'price': row.xpath('td[2]/text()').extract(),
    })


print(cpus)
