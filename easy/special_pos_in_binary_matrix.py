# take sum of each row if that row sum is 1 then get sum of each col where that index is at 

def numS(mat):
    
    special_positions = 0

    def sumOfCol(index_of_one):
        sum = 0
        for col in mat:
            sum += col[index_of_one]
        return sum

    for row in mat:
        if sum(row) == 1:
            index_of_one = row.index(1)
            special = sumOfCol(index_of_one)

            if special == 1:
                special_positions += special
    return special_positions






mat = [[1,0,0],[0,0,1],[1,0,0]]
a = numS(mat)
print(a)
