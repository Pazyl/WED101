
from math import sqrt

def hypotenuse(a = 0, b = 0):
    c = sqrt(a * a + b * b)
    return c

a = float(input("number a: "))
b = float(input("number b: "))

print(hypotenuse(a, b))