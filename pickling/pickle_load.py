import pickle
from pickle_dump import Potato


b = pickle.load(open("saved.p", "rb"))
b.print_potato()
