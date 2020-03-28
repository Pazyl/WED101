
n = int(input())

arr = [int(i) for i in input().split()]

count_number = 0;

for i in range(len(arr), 1, -1):
    if arr[i-1] > arr[i-2]:
        count_number += 1;

print(count_number)

