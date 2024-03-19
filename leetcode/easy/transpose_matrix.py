def transpose(matrix):
    return [ r for r in zip(*matrix)]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
a = transpose(matrix)
print(a)
