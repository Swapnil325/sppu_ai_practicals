graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

dist = {'A': 0, 'B': 999, 'C': 999, 'D': 999}
visited = []

current = 'A'

while current:
    visited.append(current)

    for neighbor in graph[current]:
        new_dist = dist[current] + graph[current][neighbor]

        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist

    next_node = None
    min_dist = 999

    for node in dist:
        if node not in visited and dist[node] < min_dist:
            min_dist = dist[node]
            next_node = node

    current = next_node

print(dist)