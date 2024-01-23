size = int(input())

matrix = []
bunny_pos = []
best_path = []

best_moves = None
max_collected_eggs = float("-inf")

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

for direction, position in moves.items():
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_moves = direction
        best_path = path

print(best_moves)
print(*best_path, sep="\n")
print(max_collected_eggs)
