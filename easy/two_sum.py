from typing import List

nums = [2,7,11,15]
target = 9

def twoSum(nums: list[int], target : int) -> List[int]:
    hashmap = dict()

    for i in range(len(nums)):
        complement = target - nums[i]
        if nums[i] in hashmap:
            return [hashmap[nums[i]], i]        #{0,1} returned 
        else:
            hashmap[complement] = i     # {7,0} first loop

anw = twoSum(nums, target)
print(anw)