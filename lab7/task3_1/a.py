
n = int(input())
m = int(input())

result = []

for i in range(n, m + 1):
    if i % 2 == 0:
        result.append(i)

print(' '.join(str(i) for i in result))