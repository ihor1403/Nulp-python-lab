from collections import deque
def find_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([start])
    path = [start]
    while queue:
        current = queue.popleft()
        print(current)
        visited.add(current)

        if current == end:
            return path

        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            next_point = (current[0] + dx, current[1] + dy)

            if 0 <= next_point[0] < rows and 0 <= next_point[1] < cols and maze[next_point[0]][next_point[1]] == 1 and next_point not in visited:
                queue.append(next_point)
                path.append(next_point)
                visited.add(next_point)

    return []

