
from math import sqrt

n = int(input())
m = int(input())

result = []

for i in range(n, m + 1):
    if int(sqrt(i)) == sqrt(i):
        result.append(i)

print(' '.join(str(i) for i in result))
