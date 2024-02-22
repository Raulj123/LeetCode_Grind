def climbStairs(n:int) -> int:
    prev1 = 1
    prev2 = 2
    steps = 0
    if n <=2:
        return n
    for i in range(2,n):
        steps = prev1 + prev2
        prev1 = prev2
        prev2 = steps
    return steps

n = 3
result = climbStairs(n)
print("result: ", result)