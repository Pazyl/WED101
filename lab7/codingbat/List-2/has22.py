def has22(nums):
    result = False
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == 2:
            result = True
    return result