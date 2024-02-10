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
row, col = 0, 0
path = []
collected_coins = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for rows in range(SIZE):
    field.append(input().split())

    if "P" in field[rows]:
        row, col = rows, field[rows].index("P")
        path.append([row, col])

while True:
    command = input()

    row += directions[command][0]
    col += directions[command][1]

    row, col = row_col_pos_checker(row, col)
    path.append([row, col])

    position = field[row][col]

    if position.isdigit():
        collected_coins += int(position)
        field[row][col] = "0"
    elif position == "X":
        collected_coins /= 2
        print(f"Game over! You've collected {int(collected_coins // 1)} coins.")
        break

    if collected_coins >= 100:
        print(f"You won! You've collected {collected_coins} coins.")
        break

print("Your path:")
[print(item) for item in path]
