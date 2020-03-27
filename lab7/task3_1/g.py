
n = int(input())

result = []

for i in range(2, n + 1):
    if n % i == 0:
        result.append(i)

print(result[0])