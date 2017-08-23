# You do not need an __init__ method to specify attributes.

class Rectangle:

    def area(self):
        return self.length * self.width


r = Rectangle()
r.length, r.width = 13, 8
print(r.area())
