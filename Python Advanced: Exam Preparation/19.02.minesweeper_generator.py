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
    bomb_pos_r, bomb_pos_c = map(int, (input().strip("(").strip(")").split(", ")))
    field[bomb_pos_r][bomb_pos_c] = "*"

for r in range(SIZE):
    for c in range(SIZE):

        if field[r][c] == 0:
            mine_count = 0
            for direction in directions:

                row = r
                col = c

                row += directions[direction][0]
                col += directions[direction][1]

                if 0 <= row < SIZE and 0 <= col < SIZE:

                    if field[row][col] == "*":
                        mine_count += 1

            field[r][c] = mine_count

[print(*row) for row in field]
