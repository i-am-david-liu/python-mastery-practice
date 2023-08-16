# mutint.py

# @total_ordering <---- this decorator "fills in" other comparisons as long as base
#                        comparisons exist
#                       EX: __eq__() and __lt__() is enough to "fill in" __le__()
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
    
    # how the object should be printed
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MutInt({self.value!r})'

    # how the object should deal with formats
    def __format__(self, fmt):
        return format(self.value, fmt)

    # add operation
    def __add__(self, other):
    if isinstance(other, MutInt):
        return MutInt(self.value + other.value)
    elif isinstance(other, int):
        return MutInt(self.value + other)
    else:
        return NotImplemented

    __radd__ = __add__      # reversed operands

    # in-place add (+=)
    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    # comparison operators too
    # __eq__()
    # __lt__()
    # etc.

    # convert to int
    def __int__(self):
    return self.value

    # convert to float 
    def __float__(self):
        return float(self.value)

    __index__ = __int__     # for indexing
