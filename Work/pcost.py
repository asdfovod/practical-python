# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    sum = 0
    with open(filename, 'rt') as f:
        next(f) # header
        for line in f:
            name, shares, price = line.strip().split(',')
            sum += float(shares) * float(price)
    return sum

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)


