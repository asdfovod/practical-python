# pcost.py
#
# Exercise 1.27
import sys, csv

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows) # header
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                # name, shares, price = rows.strip().split(',')
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total_cost

if len(sys.argv) == 2 or not FileNotFoundError:
    filename = sys.argv[1]
else:
    print('File not found')
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)


