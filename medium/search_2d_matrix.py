# time -> o(logn) + o(logm)
# mem -> o(1)
def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bott = 0, ROWS - 1

    while top <= bott:
        row = (top + bott) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bott = row - 1
        else:
            break
    if not (top <= bott):
        return False
   
    l, r = 0, COLS - 1

    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False
    



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
result = searchMatrix(matrix, target)
print(f"result: {result}")
