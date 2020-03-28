def max_end3(nums):
    nums.sort()
    max = nums[-1]
    nums.clear()
    for i in range(3):
        nums.append(max)
    return nums


print(max_end3([11, 5, 9]))