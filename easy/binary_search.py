# time -> o(logn)
# space -> o(1)

def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (l + r) // 2
        if nums[m] > target:
            r -= 1
        elif nums[m] < target:
            l += 1
        else:
            return m
    return -1


nums = [-1,0,3,5,9,12]
target = 9 
result = search(nums, target)
print(f"result: {result}")
