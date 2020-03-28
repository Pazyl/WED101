
n = int(input())

arr = [int(i) for i in input().split()]

count_number = 0;

for i in range(0, len(arr) - 1):
    if (arr[i] > 0 and arr[i+1] > 0) or (arr[i] < 0 and arr[i + 1] < 0):
        count_number += 1

if count_number == 0:
    print('NO')
else:
    print('YES')

