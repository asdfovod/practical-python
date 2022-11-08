# report.py
#
# Exercise 2.4

import sys
import csv
from pprint import pprint # 큰 리스트와 딕셔너리 한번에 조회

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for nrow, row in enumerate(rows, start=1):
            holding = dict(zip(headers, row))
            portfolio.append(holding.copy()) # 가변자료형은 얕은복사x
    return portfolio

def read_price(filename):
    price = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = ['name', 'price']
        for nrow, row in enumerate(rows, start=1):
            try:
                holding = dict(zip(headers, row))
                price.append(holding.copy()) # 가변자료형은 얕은복사x
            except IndexError:
                break        
    return price
    


def portfolio_cost(portfolio):
    total_cost = 0.0
    for i in portfolio:
        nshare = int(i['shares'])
        price = float(i['price'])
        cost = nshare * price
        total_cost += cost
    return total_cost

if len(sys.argv) == 3:
    pfFile = sys.argv[1]
    prFile = sys.argv[2]
elif len(sys.argv) == 2:
    pfFile = sys.argv[1]
    prFile = 'Data/prices.csv'
else:
    pfFile = 'Data/portfolio.csv'
    prFile = 'Data/prices.csv'

portfolio = read_portfolio(pfFile)
price = read_price(prFile)

# print report
cost = portfolio_cost(portfolio)
print('Total cost:', cost)
print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('Name', 'Shares', 'Price', 'Change'))
print('---------- ---------- ---------- -----------')

for pf in portfolio:
    for pr in price:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        if pr.get('name') == pf.get('name'):
            name = pf['name']
            shares = pf['shares']
            change = float(pr['price']) - float(pf['price'])
            prices = '$' + str(pf['price']) # 여기부터안됨
            
            print(f'{name:>10s} {shares:>10s} {prices:>10s} {change:>10.2f}')
