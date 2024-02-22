nums = [1,2,3,4,4,2,3]


def singleNumber(nums: list[int]) -> int:
    result = 0
    for i in range(len(nums)):
        result = result ^ nums[i]

    return result

result = singleNumber(nums)
print("result: ", result)

# XOR is a bitwise operator, and it stands for “exclusive or.”
# It performs logical operation.
# If input bits are the same, then the output will be false(0) else true(1).

# Article that helped understand -> https://blog.devgenius.io/leetcode-136-single-number-solution-with-images-1039c88b9649