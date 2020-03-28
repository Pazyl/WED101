def centered_average(nums):
    nums.sort()
    sum = 0
    min = nums[0]
    max = nums[-1]
    for i in range(len(nums)):
        sum += nums[i]

    return (sum - min - max) // (len(nums) - 2);


print(centered_average([1, 2, 3, 4, 100]))