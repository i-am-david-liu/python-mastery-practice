# stock.py

import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(filepath):
    ret = []
    with open(filepath) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            ret.append( Stock(row[0], int(row[1]), float(row[2])) )

    return ret

def print_portfolio(portfolio):
    print(f"{'name':>10} {'shares':>10} {'price':>10}")
    print('-'*10, '-'*10, '-'*10)
    for s in portfolio:
        print(f'{s.name:>10} {s.shares: 10d} {s.price: 10.2f}')


if __name__ == "__main__":
    pass
