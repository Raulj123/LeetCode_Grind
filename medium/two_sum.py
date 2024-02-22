# time -> o(n)
# mem -> o(1)

def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        current_sum = numbers[l] + numbers[r]
        if current_sum > target:
            r -= 1
        elif current_sum < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return []



numbers  = [2, 7, 11, 15]
target = 9
result = twoSum(numbers, target)
print(f"result: {result}")
