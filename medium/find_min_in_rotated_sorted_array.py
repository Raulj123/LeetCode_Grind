# if the mid point is greater than whats on the left than we are on the greater side yk?

def findMin(nums):
    l, r = 0, len(nums) - 1
    res = nums[0]

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
    
        m = ( l + r) // 2
        res = min(res, nums[m])
    
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res


nums = [3,4,5,1,2]
result = findMin(nums)
if result == 1:
    print(f"Passed: {result}")
else:
    print("Failed")
