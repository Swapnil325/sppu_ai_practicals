edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (2, 'B', 'C')
]

edges.sort()

parent = {}

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    parent[find(x)] = find(y)

nodes = ['A', 'B', 'C']

for n in nodes:
    parent[n] = n

for w, u, v in edges:
    if find(u) != find(v):
        print(u, "-", v, "=", w)
        union(u, v)