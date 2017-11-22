prices = {
    "ACME": 45.23,
    "AAPL": 612.79,
    "IBM": 205.55,
    "HPQ": 37.50,
    "FB": 10.74
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
sorted_price = sorted(zip(prices.values(), prices.keys()))

# Return the name of the max or min value.
min_stock = min(prices, key=lambda k: prices[k])
max_stock = max(prices, key=lambda k: prices[k])

min_value = prices[max(prices, key=lambda k: prices[k])]
