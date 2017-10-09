import numpy as np

def drop_first_last(grades):
    first, *middle, last = grades
    assert type(middle) == list
    return np.mean(middle)

record = ("Dave", "dave@example.com", "773-552-1212", "847-555-1212")

name, email, *phone_numbers = record
