# pcost.py
#
# Exercise 1.27
sum = 0
import gzip
with gzip.open('Work/Data/portfolio.csv.gz', 'rt') as f:
    headers = next(f)
    dataList = []
    for line in f:
        name, shares, price = line.strip().split(',')
        sum += float(shares) * float(price)
print('Total cost', sum)
