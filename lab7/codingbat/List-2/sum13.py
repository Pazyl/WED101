def sum13(nums):
    sum = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        sum += nums[i]
        i += 1

    return sum


print(sum13([13, 1, 2, 13, 2, 1, 13]))