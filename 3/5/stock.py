# stock.py

import csv
from decimal import Decimal


class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

class DStock(Stock):
    types = (str, int, Decimal)


def read_portfolio(filepath):
    ret = []
    with open(filepath) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            ret.append( Stock.from_row(row) )

    return ret

def print_portfolio(portfolio):
    print(f"{'name':>10} {'shares':>10} {'price':>10}")
    print('-'*10, '-'*10, '-'*10)
    for s in portfolio:
        print(f'{s.name:>10} {s.shares: 10d} {s.price: 10.2f}')


if __name__ == "__main__":
    pass
