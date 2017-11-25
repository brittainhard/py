"""
Reduction functions are functions like sum, min, max.

This is cool. Instead of forst fpr,omg tje list of wjatever pf tje stiff tjat
you want to analyze, you can form it inplace with the same list comprehension
syntax.

Basically, find a way if you can turn some changes on complex data structures
into generators. This will almost always be much more memory efficient, right?
Maybe because you end up with objects that have yet to be evaluated?
"""

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# Determine if any .py files exist in this directory.
import os

files = os.listdir("./")
if any(name.endswith(".py") for name in files):
    print("There be python!")
else:
    print("Sorry, no python")
