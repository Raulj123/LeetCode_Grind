def kids(candies, extra):
    sort = sorted(candies)
    great = sort[-1]
    res = []
    for candy in candies:
        c = candy + extra
        if c >= great:
            res.append(True)
        else:
            res.append(False)
    return res
    

candies = [2,3,5,1,3]
extra = 3
a = kids(candies, extra)

if a == [True, True, True, False, True]:
    print("Passed")
else:
    print("Failed")

