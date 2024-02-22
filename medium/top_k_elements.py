def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums:
        # ex/ {1: occurs 5 times}
        count[n] = 1 + count.get(n,0)
    for n,c in count.items():
         # c is count aka index and n is the actual num 
         # so were appending num in its index where 
         # index is how many times it showed up 
        freq[c].append(n)
    result =[]
    for i in range(len(freq)-1, 0, -1):
        # for each num at freq index i 
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result


nums = [1,1,1,2,2,3,3,3,3]
k = 2
result = topKFrequent(nums,k)
print("result:", result)

# time -> iterating thru input array o(n) + iterating thru n values in exactly one position o(n)
# space -> freq array and hashmap o(n)

# this one was tricky to understand 6/12 