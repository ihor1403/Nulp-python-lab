from typing import List, Tuple, Dict


def wanted_end_field(row_pos: int, column_pos: int, rows: int, cols: int) -> bool:
    return (column_pos == cols - 1 and row_pos == 0) or (column_pos == cols - 1 and row_pos == rows - 1)


def not_wanted_end_field(row_pos: int, column_pos: int, rows: int, cols: int) -> bool:
    return column_pos == cols - 1 and 0 < row_pos < rows - 1


def build_letter_positions(matrix: List[List[str]], rows: int, cols: int) -> Dict[str, List[Tuple[int, int]]]:
    letter_positions = {}
    for x in range(rows):
        for y in range(cols):
            letter = matrix[x][y]
            if letter not in letter_positions:
                letter_positions[letter] = []
            letter_positions[letter].append((x, y))
    return letter_positions


def build_next_positions(matrix: List[List[str]], rows: int, cols: int,
                         letter_positions: Dict[str, List[Tuple[int, int]]]) -> List[List[List[Tuple[int, int]]]]:
    next_positions = [[[] for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            current_letter = matrix[x][y]
            same_next_letter_positions = [
                (nx, ny) for nx, ny in letter_positions[current_letter] if ny > y
            ]
            next_pos = (x, y + 1)
            if y + 1 < cols and next_pos not in same_next_letter_positions:
                same_next_letter_positions.append(next_pos)
            next_positions[x][y] = same_next_letter_positions
    return next_positions

def indiana_jones_traversal(sneaky_way: List[List[str]], rows: int, cols: int) -> int:
    dp = [[0] * cols for _ in range(rows)]
    letter_positions = build_letter_positions(sneaky_way, rows, cols)
    next_positions = build_next_positions(sneaky_way, rows, cols, letter_positions)

    for i in range(rows):
        dp[i][0] = 1

    for col in range(cols):
        for row in range(rows):
            if not_wanted_end_field(row, col, rows, cols):
                continue
            for next_row, next_col in next_positions[row][col]:
                dp[next_row][next_col] += dp[row][col]

    total_ways = dp[0][cols - 1] + dp[rows - 1][cols - 1] if rows > 1 else dp[0][cols - 1]
    return total_ways


def read_input_matrix(path: str) -> Tuple[int, int, List[List[str]]]:
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split("\n")
        cols, rows = map(int, data[0].split())
        sneaky_way = [list(data[i]) for i in range(1, len(data))]
    return rows, cols, sneaky_way


def read_output(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    return int(data)


if __name__ == '__main__':
    row_size, col_size, sneaky_way = read_input_matrix("../resources/ijones_1_case.in")
    result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)