graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

visited = ['A']
cost = 0

while len(visited) < len(graph):
    min_edge = 999

    for v in visited:
        for n in graph[v]:
            if n not in visited and graph[v][n] < min_edge:
                min_edge = graph[v][n]
                a, b = v, n

    print(a, "-", b, "=", min_edge)
    cost += min_edge
    visited.append(b)

print("Total Cost:", cost)