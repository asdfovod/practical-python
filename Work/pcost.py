# pcost.py
# 
# Exercise 1.27
import sys, csv
import fileparse as fp

def portfolio_cost(filename): 
    '''
    *** 파일순서 꼭 맞춰야함 ***
        name, shares, price
    '''
    total_cost = 0
    record = fp.parse(filename)
    if type(filename) == tuple:
        for r in record:
            nshares = r[1]
            price = r[2]
            total_cost += nshares * price
    else :
        for r in record:
            nshares = r['shares']
            price = r['price']
            total_cost += nshares * price
        
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows) # header
    #     for rowno, row in enumerate(rows, start=1):
    #         record = dict(zip(headers, row))
    #         try:
    #             # name, shares, price = rows.strip().split(',')
    #             nshares = int(record['shares'])
    #             price = float(record['price'])
    #             total_cost += nshares * price
    #         except ValueError:
    #             print(f'Row {rowno}: Bad row: {row}')
    return total_cost

if len(sys.argv) == 2 or not FileNotFoundError:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

def main(filename, prFile):
    portfolio_cost(prFile)

if __name__ == '__main__':
    filename = sys.argv[0]
    main(filename)


