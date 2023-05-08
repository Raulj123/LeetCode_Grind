def searchInsert(nums:list[int], target:int) -> int:
    should_be = 0
    for i in range(len(nums)):
        if nums[i] == target:
            return i 
        elif nums[i] < target:
            should_be +=1
    return should_be

nums = [1,2,6,8,10]
target = 11
result = searchInsert(nums, target)
print("Result: ", result)