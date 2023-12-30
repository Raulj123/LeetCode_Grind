def onesMinusZeros(grid):
    m, n = len(grid), len(grid[0])
    print(f"Grid size: {m}x{n}")

    rowOnes = [sum(row) for row in grid]
    colOnes = [sum(col) for col in zip(*grid)]
    print(f"rowOnes: {rowOnes}, colOnes: {colOnes}")
    diff = [[0 for col in range(n)]for row in range(m)]
    print(f"Diff matrix: {diff}")
    for row in range(m):
        for col in range(n):
            diff[row][col] = rowOnes[row] + colOnes[col] - (m - rowOnes[row]) - (n - colOnes[col])
    print(f"Diff after: {diff}")


        

grid = [[0,1,1],[1,0,1],[0,0,1]]
onesMinusZeros(grid)
