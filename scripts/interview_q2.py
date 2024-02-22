from itertools import combinations
arr = [1,2,3,4,5,6,7,8,9, 10]
sum_ = 7

def findOptions(arr, sum_):
    new = []
    res = []
    for r in range(0, len(arr)+1):
        new += list(combinations(arr, r))
    
    for option in new:
        if sum(option) == sum_:
            res.append(option)
    print(res)



findOptions(arr,sum_)
