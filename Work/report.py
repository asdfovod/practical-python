# report.py
#
# Exercise 2.4

import sys
import csv
from pprint import pprint # 큰 리스트와 딕셔너리 한번에 조회
from fileparse import parse
import pcost

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
    portfolio = parse(filename)
    return portfolio

def read_price(filename, debug=False):
    '''
    주식 가격 파일을 읽어와 딕셔너리의 리스트를 생성
    키: name, price
    '''
    price = []
    parsed = parse(filename, types=[str,float], has_headers=False)
    headers = 'name', 'price'
    for par in parsed:
        holding = {h:p for h, p in zip(headers, par)}
        price.append(holding)    
    return price
    
def portfolio_cost(pfFile) -> float:
    total_cost = pcost.portfolio_cost(pfFile)
    return total_cost

def main(pfFile, prFile):
    portfolio = read_portfolio(pfFile)
    price = read_price(prFile)
    cost = portfolio_cost(pfFile)

    print('Total cost:', cost)
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('Name', 'Shares', 'Price', 'Change'))
    print('---------- ---------- ---------- -----------')

    for pf in portfolio:
        for pr in price:        
            if pr.get('name') == pf.get('name'):
                name = pf['name']
                shares = pf['shares']
                change = float(pr['price']) - pf['price']
                prices = '$' + str(pf['price'])
                print(f'{name:>10s} {shares:>10d} {prices:>10s} {change:10.2f}')
                # print('%10s %10d %10s %10.2f' % (name, shares, prices, change))

# pfFile, prFile = csvfile_export()
# portfolio_report(pfFile, prFile)

if __name__ == '__main__':
    filename, pfFile, prFile = sys.argv[0], sys.argv[1], sys.argv[2]
    main(pfFile, prFile)