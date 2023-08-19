# Exercise 2.2 notes

- `pprint` is pretty print
- `collections` library is useful:
    - `Counter` can be added together
    - `defaultdict` for grouping data

# Exercise 2.3 notes

- `zip()` for pairing data
    - `dict(zip(a, b))` makes key: a, value: b

## Generator expressions

- Think of them as list comprehensions that do not create lists
- Generators create **objects** for iterative consumption
    - They generate the values *on the fly*!
- Generators can only be used once because they use *iterators*
    - This also means we can use `next()`
    - when we reach the end, returns `Stopiteration` exception
- We can use `yield` statements to return generators
    - Useful when a function will return something huge (lots of memory), but we only need to read it once
    - When we call a yielded function, the code in the function's body does not run until the generator iterates
- Use generators for functions like `sum()`, `min()`, `max()`, `any()`

## Why generators?

- Take a look at this code block:
```python3
import csv

f = open('Data/ctabus.csv')
f_csv = csv.reader(f)                                   # use iterator (don't load entire file)
headers = next(f_csv)                                   # get headers
rows = (dict(zip(headers,row)) for row in f_csv)        # create generator for dict elements
rt22 = (row for row in rows if row['route'] == '22')    # create generator for rows with route 22
print( max(rt22, key=lambda row: int(row['rides'])) )   # create generator for rt22 with max ridership

> {'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
```
- Notice that each would-be-collection is used as a generator. We create the values on-the-fly, and don't actually store the entire collection
- how this works: `rows` and `rt22` don't run UNTIL they're iterated by the `max` function
- `max` calls for the next value in `rt22`, which calls for the next value in `rows`, which calls for the next value in `f_csv`
- when `max` iterates again, python tosses the previous value and generates the next one
    - note: the `key` argument in `max` is just a lambda expression (anonymous function) with parameter `row`, which consumes the iterable from `rt22`. the result of this lambda is the value being compared
    - for example, we can pass `key=len` to compare the length of each iterable


# Exercise 2.4 notes

- `__slots__` in classes are used for faster attribute access and smaller memory footprint
    - But, this is best used if we expect all objects of the class to have a specific set of attributes (no dynamic definitions)
    - Also, their effects are best represented when we instantiate a LOT of those objects (memory scaling)
- `isinstance()` for object type equality

# Exercise 2.6 notes

- `l = [str, int, float]` (list of functions, yeah you can do that!)
- we can do this too: `record = [func(val) for func, val in zip(l, ['A', '100', '32.30'])`
- the reason why we can "store" functions as elements is because everything in Python is a "first-class object"
