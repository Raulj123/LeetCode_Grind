def longestConsecutive(nums:list[int])-> int:
    numSet = set(nums)
    longest = 0
    for n in nums:
        # check if its the start of a sequence 
        if (n-1) not in numSet:
            length =1
            while(n + length) in numSet:
                length +=1
            longest = max(longest,length)
    return longest

nums = [100,4,200,1,3,2]
result = longestConsecutive(nums)
print("Result: ", result)

#time -> o(n)
#space -> o(n)