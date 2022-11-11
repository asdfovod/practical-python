# report.py
#
# Exercise 2.4

import sys
import csv
from pprint import pprint # 큰 리스트와 딕셔너리 한번에 조회

def csvfile_export():
    if len(sys.argv) == 3:
            pfFile = sys.argv[1]
            prFile = sys.argv[2]
    elif len(sys.argv) == 2:
        pfFile = sys.argv[1]
        prFile = 'Data/prices.csv'
    else:
        pfFile = 'Data/portfolio.csv'
        prFile = 'Data/prices.csv'
    return pfFile, prFile

def read_portfolio(filename) -> list:
    '''
    주식 포트폴리오 파일을 읽어와 딕셔너리의 리스트를 생성
    키: name, shares, price
    '''
    types = [str, int, float]
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for nrow, row in enumerate(rows, start=1):
            row = [types[n](r) for n, r in enumerate(row)] # 타입 변환
            holding = dict(zip(headers, row))
            portfolio.append(holding.copy()) # 가변자료형은 얕은복사x
    return portfolio

def read_price(filename, debug=False):
    '''
    주식 가격 파일을 읽어와 딕셔너리의 리스트를 생성
    키: name, price
    '''
    types = [str, float]
    price = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = ['name', 'price']
        for nrow, row in enumerate(rows, start=1):
            try:
                row = [t(r) for t, r in zip(types, row)]
                holding = dict(zip(headers, row))
                price.append(holding.copy()) # 가변자료형은 얕은복사x
            except IndexError: 
                print('IndexError')
                break        
    return price
    
def portfolio_cost(portfolio) -> float:
    total_cost = 0.0
    for i in portfolio:
        nshare = int(i['shares'])
        price = float(i['price'])
        cost = nshare * price
        total_cost += cost
    return total_cost

def portfolio_report(pfFile, prFile):
    portfolio = read_portfolio(pfFile)
    price = read_price(prFile)
    cost = portfolio_cost(portfolio)
    # print(portfolio, price, cost)

    print('Total cost:', cost)
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('Name', 'Shares', 'Price', 'Change'))
    print('---------- ---------- ---------- -----------')

    for pf in portfolio:
        for pr in price:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            if pr.get('name') == pf.get('name'):
                name = pf['name']
                shares = pf['shares']
                change = pr['price'] - pf['price']
                prices = '$' + str(pf['price'])
                print(f'{name:>10s} {shares:>10d} {prices:>10s} {change:10.2f}')
                # print('%10s %10d %10s %10.2f' % (name, shares, prices, change))
pfFile, prFile = csvfile_export()
portfolio_report(pfFile, prFile)