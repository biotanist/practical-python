# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            row = csv.reader(f)
            try:
                total_cost = float(row[1]) * float(row[2]) + total_cost
            except ValueError:
                print("Couldn't parse", line)    

    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')