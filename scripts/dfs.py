from collections import deque

def dfs(graph, start, goal):
    v = []
    stack = deque()

    v.append(start)
    stack.append(start)

    while stack:
        curr = stack.pop()
        print(curr)

        if curr == goal:
            break
        # reversed since we give priority over alpha
        for node in reversed(graph[curr]):
            if node not in v:
                v.append(node)
                stack.append(node)
    return "DFS done!"

graph = {
    "A": ["B", "C"],
    "B": ["D","E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}

print(dfs(graph, "A", "D"))
