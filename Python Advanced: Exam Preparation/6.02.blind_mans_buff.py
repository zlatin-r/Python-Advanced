rows, cols = [int(x) for x in input().split()]

field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

cached_players = 0
moves = 0

for row in range(rows):
    field.append(input().split())

    if "B" in field[row]:
        r, c = row, field[row].index("B")

command = input()
while command != "Finish":

    r += directions[command][0]
    c += directions[command][1]

    if 0 <= r < rows and 0 <= c < cols:
        symbol = field[r][c]

        if symbol == "O":
            r -= directions[command][0]
            c -= directions[command][1]
        elif symbol == "-":
            moves += 1
        elif symbol == "P":
            field[r][c] = "-"
            cached_players += 1
            moves += 1

            if cached_players == 3:
                break

    else:
        r -= directions[command][0]
        c -= directions[command][1]

    command = input()

print(f"Game over!\nTouched opponents: {cached_players} Moves made: {moves}")
