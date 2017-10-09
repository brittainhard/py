p = (4, 5)
x, y = p

data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

name2, shares2, price2, (year, mon, day) = data

assert year == 2012
assert day == 21
assert mon == 12

