income = 4400
a = dict(
    rent=820,
    savings=880,
    netflix=9,
    cable=60,
    spotify=10,
    unicef=160,
    power=30,
)
expenses = sum(a.values())

budget = income - expenses
print(budget)
