# reader.py

import csv
from abc import ABC, abstractmethod
from pprint import pprint


# template for CSV parsing
class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)


def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dicts 
    '''
    records = [] 
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(DictCSVParser(types).parse(filename))

    return records 

# the 'cls' must have a 'from_row()' method
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(InstanceCSVParser(cls).parse(filename))

    return records


if __name__ == "__main__":
    #pprint( read_csv_as_dicts('../../Data/portfolio.csv', [str,int,float])[:5] )
    pass
