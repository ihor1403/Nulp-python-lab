def find_shortest_path(maze, start, end):

  if start == end:
    return [start]

  if not (0 <= start[0] < len(maze) and 0 <= start[1] < len(maze[0]) and maze[start[0]][start[1]] == 1):
    return []

  for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
    next_point = (start[0] + direction[0], start[1] + direction[1])
    path = find_shortest_path(start, next_point, end)
    if path:
      return [start] + path

  return []