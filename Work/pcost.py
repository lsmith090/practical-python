# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                num_shares = int(row[1])
            except ValueError:
                print("Couldn't parse", row)
            try:
                cost_shares = float(row[2])
            except ValueError:
                print("Couldn't parse", row)
            total_cost += num_shares * cost_shares
    return total_cost  

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)