
n = int(input())

arr = [int(i) for i in input().split()]

print(' '.join(str(i) for i in arr[::2]))

#for i in range(0, len(arr), 2):
#    print(arr[i], end=' ')