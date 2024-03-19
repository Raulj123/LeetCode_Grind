"""https://www.youtube.com/watch?v=g3Ms5e7Jdqo&t=301s"""
filename = "file12.txt"

with open(filename) as file:
    data = file.read().splitlines()
total = 0
cache = {}
def count(data, nums):
   
    if data == "":
        return 1 if nums == () else 0 
    if nums == ():
        return 0 if "#" in data else 1
    results = 0
    key = data, nums
    if key in cache:
        return cache[key]
    if data[0] in ".?":
        results += count(data[1:], nums)
    if data[0] in "#?":
        if nums[0] <= len(data) and "." not in data[:nums[0]] and (nums[0] == len(data) or data[nums[0]] != "#"):
            results += count(data[nums[0] + 1:], nums[1:])
        else:
            results += 0
    cache[key] = results 
    return results 

for line in data:
    data, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    data = "?".join([data] * 5)
    nums *= 5
    total += count(data, nums)
print(total)