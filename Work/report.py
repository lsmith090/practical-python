# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        #add to portfolio
        for row in rows:
            try:
                holding = {}
                holding['name'] = row[0]
                holding['shares'] = int(row[1])
                holding['price'] = float(row[2])
                portfolio.append(holding)
            except ValueError:
                print("Couldn't parse", row)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if any(x.strip() for x in row):
                prices[row[0]] = float(row[1])
    return prices

def can_i_retire(portfolio, prices):
    value = 0.0
    delta_value = 0.0
    for holding in portfolio:
        if prices.get(holding['name'], 0.0) > 0:
            #set variables
            price = holding['price']
            og_price = prices[holding['name']]
            shares = holding['shares']
            
            delta_value += price*shares
            #print('Holding Name:', holding['name'], 'Current price:', price, 'Current shares held:', shares, "Current holding value:", (price*shares))
            value += og_price*shares
            #print('Holding Name:', holding['name'], 'Original price:', og_price, 'Current shares held:', shares, "Original holding value:", (og_price*shares))
    print("Current value:", f'{delta_value:0.2f}')
    print("Gain/loss since purchase:", f'{delta_value-value:0.2f}')

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        if prices.get(holding['name'], 0.0) > 0:
            #set variables
            
            purchase_price = holding['price']
            current_price = prices[holding['name']]
            shares = holding['shares']
            change =  current_price - purchase_price
            report.append((holding['name'], shares, current_price, change))
            
    return report