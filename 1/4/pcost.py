# pcost.py

import sys

# takes a list of strings as input
def portfolio_cost(filename):
    total = 0.0
    with open(filename) as file:
        for line in file:
            _, nstock, price = line.split()

            try:
                total += (int(nstock) * float(price))
            except ValueError:
                print(f"Couldn\'t parse: {repr(line)}")

    return total

if __name__ == "__main__":

    #filename = "../../Data/portfolio.dat"
    filename = "../../Data/portfolio3.dat"
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    print(portfolio_cost(filename)) 
