word = input()

SIZE = int(input())
field = []

start_pos = (0, 0)

for row in range(SIZE):
    field.append(list(input()))

    if "P" in field[row]:
        start_pos = row, field[row].index("P")

r, c = start_pos[0], start_pos[1]
field[r][c] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

commands = int(input())

for _ in range(commands):
    command = input()

    r += directions[command][0]
    c += directions[command][1]

    if 0 <= r < SIZE and 0 <= c < SIZE:
        symbol = field[r][c]

        if symbol.isalpha():
            word += symbol
            field[r][c] = "-"

    else:
        r -= directions[command][0]
        c -= directions[command][1]
        word = word[:-1]

field[r][c] = "P"

print(word)
[print(''.join(row)) for row in field]
