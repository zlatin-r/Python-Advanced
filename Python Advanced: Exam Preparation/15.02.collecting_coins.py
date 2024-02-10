def row_col_pos_checker(r, c):
    if r > SIZE - 1:
        r = 0
    if r < 0:
        r = SIZE - 1
    if c > SIZE - 1:
        c = 0
    if c < 0:
        c = SIZE - 1

    return r, c


SIZE = int(input())

field = []
r, c = 0, 0
path = []
collected_coins = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    field.append(input().split())

    if "X" in field[row]:
        r, c = row, field[row].index("P")

while True:
    command = input()

    r += directions[command][0]
    c += directions[command][1]

    r, c = row_col_pos_checker(r, c)

    position = field[r][c]

    if position == ""

