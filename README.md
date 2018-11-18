# CPU Price Graph
Simple analysis of CPU price vs performance.

# Table Of Contents
- [Overview](#overview)
- [Run](#run)
	- [Setup](#setup)
	- [Execute](#execute)
		- [Scrape](#scrape)
		- [Graph](#graph)

# Overview
Analysis of data set from [cpubenchmark.net]('https://www.cpubenchmark.net/high_end_cpus.html').

2 scripts are provided:

- [`scrape.py`](./scrape.py): Scrapes the website and saves CPU data in `specs.json`
    - Saves array of objects with the `cpu`, `rating`, and `price` keys
- [`graph.py`](./graph.py): Plots the data set

See the [run](#run) section for details on how to execute these scripts.

# Run
Before running scripts you must setup your environment.

## Setup
[Pipenv](https://pipenv.readthedocs.io/en/latest/) is used to manage
Python dependencies.

Install dependencies by running:

```
pipenv install
```

Then run the Python virtual environment:

```
pipenv shell
```

## Execute
### Scrape
To run the `scrape.py` script execute the following command:

```
scrapy runspider scrape.py -o specs.json
```

### Graph
To run the `graph.py` script execute the following command:

```
./graph.py
```
