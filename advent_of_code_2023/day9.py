from itertools import pairwise
filename = "file9.txt"

with open (filename) as file:
    data = file.read().split("\n")

nums = [[int(x) for x in line.split()] for line in data]
nums_2 = [[int(x) for x in line.split()[::-1]] for line in data]

def Sequence(nums):
    if all(num == 0 for num in nums):
        return 0
    diff = [b - a for a, b in pairwise(nums)]
    return nums[-1] + Sequence(diff)

p1_anw = sum(Sequence(line) for line in nums)
p2_anw = sum(Sequence(line) for line in nums_2)
print(p1_anw, p2_anw)