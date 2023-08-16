# pcost.py

import sys

# takes a list of strings as input
def total_cost(data):
    total = 0.0
    for line in data:
        tokens = line.split()
        total += (float(tokens[1]) * float(tokens[2]))

    return total

if __name__ == "__main__":

    filepath = "../../Data/portfolio.dat"
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    
    with open(filepath) as file:
        # split by newline, then drop EOF
        data = file.read().split('\n')[:-1]
        print(total_cost(data))
