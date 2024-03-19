def searchInsert(nums:list[int], target:int) -> int:
    l, r = 0, len(nums) -1

    while l <= r:
        m = ( l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m 
    return l 

nums = [1,2,6,8,10]
target = 11
result = searchInsert(nums, target)

if result == 5:
    print(f"Passed: {result}")
else:
    print("Failed")
