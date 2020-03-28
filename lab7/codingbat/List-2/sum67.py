def sum67(nums):
    record = True
    sum = 0
    for num in nums:
        if num == 6:
            record = False

        if record:
            sum += num
            continue

        if num == 7:
            record = True

    return sum


print(sum67([1, 2, 2, 6, 99, 99, 7]))