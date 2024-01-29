rows, cols = [int(x) for x in input().split()]

field = []
start_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    field.append(list(input()))

    if "B" in field[row]:
        start_pos = row, field[row].index("B")
        r, c = start_pos

while True:
    command = input()

    r += directions[command][0]
    c += directions[command][1]

    if 0 <= r < rows and 0 <= c < cols:

        if field[r][c] == "*":
            r -= directions[command][0]
            c -= directions[command][1]
        elif field[r][c] == "P":
            field[r][c] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
        elif field[r][c] == "A":
            field[r][c] = "P"
            print("Pizza is delivered on time! Next order...")
            break
        else:
            field[r][c] = "."

    else:
        field[start_pos[0]][start_pos[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

[print("".join(row)) for row in field]
