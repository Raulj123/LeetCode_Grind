def premutations(nums):
    res = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        prem = premutations(nums)

        for p in prem:
            p.append(n)
        res.extend(prem)
        nums.append(n)
    return res


nums = [1,2,3]
result = premutations(nums)
print(f"result: {result}")
