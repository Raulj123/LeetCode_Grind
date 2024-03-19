def mostFrequent(nums):
    mode = None
    max_freq = 0
    map = {}

    for n in nums:
        if n in map:
            map[n] += 1
        else:
            map[n] = 1
        if map[n] > max_freq:
            max_freq = map[n]
            mode = n 
    return mode




nums = [3,5,6,4,3,7,8,9,12,5,6,9,5,6,2,6]
result = mostFrequent(nums)
print(f"result: {result}")

