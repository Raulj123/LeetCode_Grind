# Moore’s Voting Algorithm! article that helped -> https://utkarsh1504.github.io/DSA-Java/bmmv-algorithm
def majorityElement(nums:list[int]) -> int:
    canidate = 0
    count = 0
    for n in nums:
        if count == 0:
            canidate = n
            count +=1
        elif canidate == n:
            count +=1
        else:
            count -=1
    return canidate

nums = [2,2,1,1,1,2,2]
result = majorityElement(nums)
print("result: ", result)
