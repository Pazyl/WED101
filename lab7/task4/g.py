
n = int(input())

arr = [int(i) for i in input().split()]

for i in range(int(len(arr) / 2)):
    b = arr[i]

    arr[i] = arr[len(arr)-i-1]

    arr[len(arr)-i-1] = b

for i in range(len(arr)):
    print(arr[i], end=' ')