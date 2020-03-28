def big_diff(nums):
    nums.sort()
    return nums[-1] - nums[0]


print(big_diff([10, 3, 5, 6]))