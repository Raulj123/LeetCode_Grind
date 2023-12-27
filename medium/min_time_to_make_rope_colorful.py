def minCost(colors, neededTime):
    totalTime = 0
    i, j = 0, 0 

    while i < len(neededTime) and j < len(neededTime):
        groupTotal = 0
        maxTotal_inGroup = 0

        while j < len(neededTime) and colors[i] == colors[j]:
            groupTotal += neededTime[j]
            maxTotal_inGroup = max(maxTotal_inGroup, neededTime[j])
            j += 1
        totalTime += groupTotal - maxTotal_inGroup
        i = j
    return totalTime

colors = "aaabbbabbbb"
neededTime = [3,5,10,7,5,3,5,5,4,8,1]
a = minCost(colors, neededTime)
expected = 26

if a == expected:
    print(f"Passed!: {a}")
else:
    print("Failed")
