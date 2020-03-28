
def my_xor(x, y):
    if (x == 1 and y == 0) or (x == 0 and y == 1):
        return 1
    else:
        return 0


arr = [int(i) for i in input().split()]

print(my_xor(arr[0], arr[1]))
