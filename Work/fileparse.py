# fileparse.py
#
# Exercise 3.3
import csv
import gzip

def open_csv(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    return rows, headers

def open_csv_gz(filename):
    f = gzip.open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    return rows, headers

def parse(filename, select=['name','shares','price'] \
    , types = [str, int, float], has_headers=True, delimiter=','):
    '''
    csv 파일을 파시해 레코드의 목록을 생성

    select = 파징할 칼럼명
    types = 파징할 칼럼의 자료형, select와 순서 같아야함
    has_headers = 원본파일의 헤더 유무 여부
    delimiter = 구분자
    '''
    if '.gz' in filename:
        rows, headers = open_csv_gz(filename)
    elif '.csv' in filename:
        rows, headers = open_csv(filename)
    else:
        rows = filename

    records = []
    errorRow = 0 # ValueError난 행의 인덱스
    for row in rows:
        try:
            errorRow += 1 
            if not row: # 데이터가 없는행 건너뜀
                continue
            if has_headers == False or type(filename) == list: # 헤더가 없는 경우(직접입력한 리스트도 포함)
                if select != ['name','shares','price']: # 헤더가 없는파일의 select 입력시 예외 일으키기
                    raise SyntaxError("\n\nThe keyword factor Select is not available when has_header is False.\n")
                row = [type(row) for type,row in zip(types, row)]
                record = tuple(row)
            else:
                indices = [headers.index(colname) for colname in select]
                row = [types[i](row[i]) for i in indices]
                record = dict(zip(select, row))
            records.append(record)
        except ValueError as e:
            print('Row ',errorRow,': Couldn\'t convert ', row)
            print('Row ',errorRow,': ',e)
    return records

    