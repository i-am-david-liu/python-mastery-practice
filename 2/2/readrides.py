# readrides.py

import csv
from collections import Counter


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


def riders_on_date(records, route='22', date='02/02/2011'):
    return sum([record[3] for record in records if record[0]==route and record[1]==date])

def rides_per_route(records):
    result = Counter()
    for record in records:
        result[record[0]] += record[3]
        
    return result

def best_yearly_increase(records, start_date='2001', end_date='2011'):
    pass

if __name__ == '__main__':
    '''
    ctabus.csv

    route   | int (bus route name)
    date    | date string (MM/DD/YYYY)
    daytype | char (U=Sunday/Holiday, A=Saturday, W=Weekday)
    rides   | int (total number of riders)
    '''

    filename = '../../Data/ctabus.csv'
    records = read_rides_as_tuples(filename)

    # 1. How many people rode the number 22 bus on February 2, 2011? What about any route
    #     on any date of your choosing?
    num_riders = riders_on_date(records) # use default route, date parameters
    print(num_riders)

    # 2. What is the total number of rides taken on each bus route?
    all_riders = rides_per_route(records)
    print(all_riders)

    # 3. What five bus routes had the greatest ten-year increase in ridership from 
    #     2001 to 2011?

