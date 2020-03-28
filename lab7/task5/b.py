
def my_power(a, n):
    val = 1

    if n == 0:
        return 1

    elif n > 0:
        for i in range(n, 0, -1):
            val *= a
        return val

    else:
        n = n * (-1)
        for i in range(n, 0, -1):
            val *= a
        return 1 / val


arr = [float(i) for i in input().split()]

print(my_power(arr[0], int(arr[1])))