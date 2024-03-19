def dailyTemperatuers(temperatures):
    res = [0] * len(temperatures)
    stack = [] # temp, index
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackI = stack.pop()
            res[stackI] = (i - stackI)
        stack.append([t,i])
    return res



temperatures = [73,74,75,71,69,72,76,73]
result = dailyTemperatuers(temperatures)
print(f"result: {result}")
