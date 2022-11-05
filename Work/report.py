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
        for row in rows:
            holding = dict()
            holding[headers[0]] = row[0]
            holding[headers[1]] = int(row[1])
            holding[headers[2]] = float(row[2])
            portfolio.append(holding.copy()) # 가변자료형은 얕은복사x
    return portfolio

def portfolio_cost(portfolio):
    total = 0.0
    for i in portfolio:
        cost = i['shares'] * i['price']
        total += cost
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio = read_portfolio(filename)
cost = portfolio_cost(portfolio)
print('Total cost:', cost)

# import sys
# import csv

# def read_portfolio(filename):
#     portfolio = {}
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
#     return portfolio

# def portfolio_cost(portfolio):
#     total_cost = 0
#     for i in portfolio:
#         cost = i[1] * i[2]
#         total_cost += cost
#     return total_cost

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'

# portfolio = read_portfolio(filename)
# cost = portfolio_cost(portfolio)
# print('Total cost:', cost)

