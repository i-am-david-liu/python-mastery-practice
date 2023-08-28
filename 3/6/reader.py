# reader.py

import csv
from pprint import pprint

def read_csv_as_dicts(filepath, types):
    ret = [] 
    with open(filepath) as f:
        rows = csv.reader(f)    # create iterator
        headers = next(rows)
        for row in rows:
            ret.append({name: func(val) for name, func, val in zip(headers, types, row)})

    return ret

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
            records.append(cls.from_row(row))
    return records


if __name__ == "__main__":
    pprint( read_csv_as_dicts('../../Data/portfolio.csv', [str,int,float])[:5] )
