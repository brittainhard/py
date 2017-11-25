"""
Done this before. Many, many times.
"""

prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75,
}

# Dictionary of prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}

# Dictionary of tech stocks
tech_names = {"AAPL", "IBM", "HPQ", "MSFT"}

p1 = {key: value for key, value in prices.items() if key in tech_names}

