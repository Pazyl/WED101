
n = int(input())

arr = [int(i) for i in input().split()]

count_number = 0;

for el in arr:
    if el > 0:
        count_number += 1;

print(count_number)

