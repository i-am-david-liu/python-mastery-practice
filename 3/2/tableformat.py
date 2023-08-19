# tableformat.py

def print_table(objs, attrs):
    headers = ''
    for attr in attrs:
        headers += f'{attr:>10} '
    print(headers)

    dividers = ''
    for _ in range(len(attrs)):
        dividers += ('-'*10 + ' ')
    print(dividers)

    for obj in objs:
        row = ''
        for attr in attrs:
            row += f'{getattr(obj, attr):>10} '
        print(row) 
