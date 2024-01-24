SIZE = int(input())

matrix = []
bunny_pos = []
path = []
best_path = None

max_eggs = 0
best_dir = ""

for row in range(SIZE):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny_pos = row, matrix[row].index("B")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for direction, pos in directions.items():
    collected_eggs = 0
    path = []

    r = bunny_pos[0] + pos[0]
    c = bunny_pos[1] + pos[1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if matrix[r][c].isdigit():
            collected_eggs += int(matrix[r][c])
            if collected_eggs > max_eggs:
                max_eggs = collected_eggs
                best_dir = direction
                best_path = path
            path.append([r, c])
        else:
            break

        r += pos[0]
        c += pos[1]

print(best_dir)
[print(row) for row in best_path]
print(max_eggs)
