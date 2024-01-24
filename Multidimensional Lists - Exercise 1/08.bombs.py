SIZE = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(SIZE)]
bombs = ((int(x) for x in c.split(",")) for c in input().split())

directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, 1),
    (-1, -1),
    (1, -1),
    (1, 1),
    (0, 0),
)

for row, col in bombs:
    if matrix[row][col] <= 0:
        continue

    damage = matrix[row][col]

    for position in directions:
        r = row + position[0]
        c = col + position[1]

        if 0 <= r < SIZE and 0 <= c < SIZE:
            if matrix[r][c] > 0:
                matrix[r][c] -= damage

alive_cells = [num for row in range(SIZE) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]
