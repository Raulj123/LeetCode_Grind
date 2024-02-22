def productExceptSelf(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    post = 1
    for i in range(len(nums)-1, -1,-1):
        result[i] *= post
        post *= nums[i]
    return result




nums = [1,2,3,4]
result = productExceptSelf(nums)
print("result:", result)

# time -> o(n)
# space -> o(1)