def threeSum(nums):
    res = []
    nums.sort()
    for i, n in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = n + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


nums = [-1,0,1,2,-1,-4]
result = threeSum(nums)
print(f"result: {result}")
