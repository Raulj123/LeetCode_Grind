from collections import Counter

def maxFrequencyElements(nums):
    count = Counter(nums)
    print(f"Counter dic: {count}")
    m = max(count.values())
    print(f"Max value is: {m}")
    values = [key for key, value in count.items() if value == m]
    print(f"chars w the same freq: {values}")
    return m * len(values)



nums = [1,2,2,3,1,4]
print(maxFrequencyElements(nums))
