
n = int(input())

i = 1

res = []

while i <= n:
    res.append(i)
    i = i * 2

print(' '.join(str(i) for i in res))