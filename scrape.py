#!/usr/bin/env python3
# Places cpubenchmark.net results in csv file
import scrapy

class SpecsSpider(scrapy.Spider):
    name = "specs"
    start_urls = [
        'https://www.cpubenchmark.net/high_end_cpus.html'
    ]

    def parse(self, resp):
        skipped_header = False

        for row in resp.xpath('/html/body/center/div[5]/div[2]/table/tr'):
            if not skipped_header:
                skipped_header = True
                continue

            data = row.css('td> *::text').extract()

            if len(data) < 4:
                continue

            cpu = data[0]
            cpu_parts = cpu.split(" @")
            if len(cpu_parts) > 0:
                cpu = cpu_parts[0]

            rating = float(data[2].replace(",", ""))
            price = data[3].replace("$","").replace(",", "").replace("*", "")

            if price != "NA":
                price = float(price)
            else:
                price = -1

            yield {
                'cpu': cpu,
                'rating': rating,
                'price': price
            }
