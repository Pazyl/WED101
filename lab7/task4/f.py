
n = int(input())

arr = [int(i) for i in input().split()]

count_number = 0

for i in range(1, len(arr) - 1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        count_number += 1

print(count_number)