graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

colors = {}

available_colors = ["Red", "Green", "Blue"]

def is_safe(node, color):

    for neighbor in graph[node]:
        if neighbor in colors and colors[neighbor] == color:
            return False

    return True

def solve(node):

    if node == len(graph):
        return True

    for color in available_colors:

        if is_safe(node, color):

            colors[node] = color

            if solve(node + 1):
                return True

            del colors[node]

    return False

solve(0)

print("Graph Coloring Solution:\n")

for node in colors:
    print("Node", node, "->", colors[node])