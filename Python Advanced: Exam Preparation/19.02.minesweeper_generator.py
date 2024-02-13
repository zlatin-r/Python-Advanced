SIZE = int(input())
bombs = int(input())

field = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up right": (-1, 1),
    "up left": (-1, -1),
    "down left": (1, -1),
    "down right": (1, 1)
}

for _ in range(bombs):
    r, c = map(int, (input().strip("(").strip(")").split(", ")))
    field[r][c] = "*"

for row in range(SIZE):
    for col in range(SIZE):

        if field[row][col] == 0:
            mine_count = 0
            for direction in directions:

                row += directions[direction][0]
                col += directions[direction][1]

                if 0 <= row < SIZE and 0 <= col < SIZE:

                    if field[row][col] == "*":
                        mine_count += 1

            field[row][col] = mine_count

print(*field, sep="\n")
