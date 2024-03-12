def binary_search(arr,target):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = r + l // 2
        print(m)

        if arr[m] > target:
            r = m - 1
        elif arr[m] < target:
            l = m + 1
        else:
            return "Target acquired " + str(m) + " " +str(arr[m])


arr = [1,2,3,4,5,12,15,16,22,23,24,25,28,39,40,50,60,99,100,101]
print(binary_search(arr,100))
