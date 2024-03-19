from collections import deque

def bfs(image, sr, sc, color):
    queue = deque()
    v = []

    m = len(image)
    n = len(image[0])
    
    value = image[sr][sc]
    image[sr][sc] = color
    
    v.append((sr,sc))
    queue.append((sr,sc))

    dir = [[0,-1], [0,1], [-1,0], [1,0]]

    while queue:
        cr, cc = queue.popleft()

        for dr, dc in dir:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == value:
                if (nr,nc) not in v:
                    v.append((nr,nc))
                    queue.append((nr,nc))
                    image[nr][nc] = color
    return image





image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(image)
print(bfs(image,sr,sc,color))
