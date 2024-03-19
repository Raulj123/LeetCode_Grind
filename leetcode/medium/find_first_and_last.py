def search(nums, target, left):
    l, r = 0, len(nums) - 1
    i = -1
    while l <= r:
        m = (l + r) // 2
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = mid - 1
        else:
            i = m
            if left:
                r = m - 1
            else:
                l = m + 1
    return i

target = 6
nums = [1,1,1,1,2,2,2,3,4,5,6,6,6]
left = search(nums, target, True)
right = search(nums, target, False)

if left == 10 and right == 12:
    print(f"Passed!: {left,right}")
else:
    print("Failed")
