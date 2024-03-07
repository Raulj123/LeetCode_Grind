from collections import deque

def bfs(graph, start, goal):
    v = []
    queue = deque()

    v.append(start)
    queue.append(start)

    while queue:
        curr = queue.popleft()
        print(curr)
        if curr == goal:
            break

        for node in graph[curr]:
            if node not in v:
                v.append(node)
                queue.append(node)

    return "BFS Done"







graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}

print(bfs(graph, "A", "G"))
