from queue import PriorityQueue

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Find position of 0
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Heuristic function (Misplaced Tiles)
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# Generate next states
def moves(state):
    x, y = find_zero(state)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    children = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            # Swap
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            children.append(new_state)

    return children

# A* Algorithm
def astar(start):
    pq = PriorityQueue()

    pq.put((heuristic(start), start, []))

    visited = []

    while not pq.empty():
        cost, state, path = pq.get()

        if state == goal:
            return path + [state]

        if state not in visited:
            visited.append(state)

            for child in moves(state):
                if child not in visited:
                    new_path = path + [state]
                    total_cost = len(new_path) + heuristic(child)

                    pq.put((total_cost, child, new_path))

# Initial State
start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

# Solve
solution = astar(start)

# Display Steps
print("Step Wise Execution:\n")

for step in solution:
    for row in step:
        print(row)
    print()