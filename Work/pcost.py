# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            stock = line.split(',')
            try:
                num_shares = int(stock[1])
            except ValueError:
                print("Couldn't parse", line)

            try:
                cost_shares = float(stock[2])
            except ValueError:
                print("Couldn't parse", line)

            total_cost += num_shares * cost_shares
        return total_cost  

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)