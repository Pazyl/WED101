
def my_min(a, b, c, d):
    n1 = min(a, b)
    n2 = min(c, d)
    return min(n1, n2)


arr = [int(i) for i in input().split()]

print(my_min(arr[0], arr[1], arr[2], arr[3]))
