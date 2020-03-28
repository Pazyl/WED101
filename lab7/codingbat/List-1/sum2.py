def sum2(nums):
    sum = 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 0:
        return 0
    for i in range(2):
        sum += nums[i]

    return sum


print(sum2([1]))