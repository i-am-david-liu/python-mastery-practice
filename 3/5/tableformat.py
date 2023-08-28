# tableformat.py

# This is an 'Abstract Base Class'
#  ABCs are a kind of interface/specification for derived classes
#  The methods attached to the ABCs should be implemented by the programmer
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(f'{h}' for h in headers))

    def row(self, rowdata):
        print(','.join(f'{d}' for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

def create_formatter(formattype):
    if formattype == 'text':
        return tableformat.TextTableFormatter()
    elif formattype == 'csv':
        return tableformat.CSVTableFormatter()
    elif formattype == 'html':
        return tableformat.HTMLTableFormatter()
    else:
        return
