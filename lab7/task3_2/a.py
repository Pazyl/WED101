
from math import sqrt

n = int(input())

i = 0

while i < n:
    i = i + 1
    if int(sqrt(i)) == sqrt(i):
        print(i)


