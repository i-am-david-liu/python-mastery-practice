# readrides.py

import collections.abc
import csv

class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            keys = ('route', 'date', 'daytype', 'rides')
            zipped_values = zip(self.routes[index],
                                self.dates[index],
                                self.daytypes[index],
                                self.numrides[index])
            return [ dict(zip(keys, values)) for values in zipped_values ]

        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route, 
                'date': date, 
                'daytype': daytype, 
                'rides' : rides
                }
            records.append(record)
    return records

if __name__ == "__main__":
    rows = read_rides_as_dicts('../../Data/ctabus.csv')
