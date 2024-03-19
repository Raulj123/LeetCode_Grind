# bisect module finds the index at which a given element should be inserted into a sorted sequence to maintain its order(using Binary search)

from bisect import bisect_left, bisect_right
def findSpecialInt(arr):
    n = len(arr)
    target = n // 4 
    can = [arr[n // 4], arr[n // 2], arr[n // 3], arr[3 * n // 4]]
    for c in can:
        left_start = bisect_left(arr, c)
        print(f"left: {left_start} can: {c}")
        right_start = bisect_right(arr,c) - 1 
        print(f"right {right_start} can: {c}")

        if right_start - left_start + 1 > target:
            return c
    return - 1




arr = [1,2,2,6,6,6,6,7,10]
a = findSpecialInt(arr)
print(a)
