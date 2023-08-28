# stock.py

import csv
from decimal import Decimal


class Stock:

    __slots__ = 'name', '_shares', '_price'
    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        attrs = [repr(getattr(self, attr)) for attr in self.__slots__]
        str_attrs = ', '.join(attrs)

        return f'Stock({str_attrs})'

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1]}")
        elif value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2]}")
        elif value < 0:
            raise ValueError("price must be >= 0")
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
                                             (other.name, other.shares, other.price))

class DStock(Stock):
    _types = (str, int, Decimal)


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
