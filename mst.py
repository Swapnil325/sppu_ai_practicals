graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2},
    'C': {'A': 3, 'B': 2}
}

visited = ['A']
cost = 0

while len(visited) < len(graph):
    minimum = 999
    x = y = ''

    for i in visited:
        for j in graph[i]:
            if j not in visited and graph[i][j] < minimum:
                minimum = graph[i][j]
                x, y = i, j

    print(x, "-", y, "=", minimum)
    cost += minimum
    visited.append(y)

print("Total Cost:", cost)