# readrides.py

import csv
import tracemalloc
from collections import namedtuple

# Tuples:
# Memory Use: Current 133068048, Peak 133098184
# Dicts:
# Memory Use: Current 225477966, Peak 225508376
# Objects:
# Memory Use: Current 188515030, Peak 188545200
# Named tuples:
# Memory Use: Current 137694532, Peak 137724702
# __slot__ objects:
# Memory Use: Current 128448478, Peak 128478648


def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = []
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
                'rides': rides,
            }
            records.append(record)

    return records


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_objects(filename):
    '''
    Read the bus ride data as a list of objects 
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides) 
            records.append(record)
    return records


def read_rides_as_ntuples(filename):
    '''
    Read the bus ride data as a list of named tuples
    '''
    Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


class SlotRow:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_slot_objects(filename):
    '''
    Read the bus ride data as a list of __slots__ objects 
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = SlotRow(route, date, daytype, rides) 
            records.append(record)
    return records


def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':

    tracemalloc.start()
    rows = read_rides_as_tuples('../../Data/ctabus.csv')
    print('Tuples:')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    rows = read_rides_as_dicts('../../Data/ctabus.csv')
    print('Dicts:')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    rows = read_rides_as_objects('../../Data/ctabus.csv')
    print('Objects:')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    rows = read_rides_as_ntuples('../../Data/ctabus.csv')
    print('Named tuples:')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    rows = read_rides_as_slot_objects('../../Data/ctabus.csv')
    print('__slot__ objects:')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()
