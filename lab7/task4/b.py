
n = int(input())

arr = [int(i) for i in input().split()]

for el in arr:
    if el % 2 == 0:
        print(el, end=' ')

