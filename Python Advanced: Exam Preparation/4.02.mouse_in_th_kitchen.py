rows, cols = [int(x) for x in input().split(",")]

cupboard = []
start_pos = []
total_cheese = 0

for row in range(rows):
    cupboard.append(list(input()))

    if "M" in cupboard[row]:
        start_pos = row, cupboard[row].index("M")
        r, c = start_pos
        cupboard[r][c] = "*"
    if "C" in cupboard[row]:
        total_cheese += cupboard[row].count("C")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        break

    r += directions[command][0]
    c += directions[command][1]

    if 0 <= r < rows and 0 <= c < cols:
        symbol = cupboard[r][c]

        if symbol == "C":
            total_cheese -= 1

            if total_cheese == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break
            cupboard[r][c] = "*"

        elif symbol == "T":
            print("Mouse is trapped!")
            break

        elif symbol == "@":
            r -= directions[command][0]
            c -= directions[command][1]

    else:
        r -= directions[command][0]
        c -= directions[command][1]
        print("No more cheese for tonight!")
        break

cupboard[r][c] = "M"
[print("".join(row)) for row in cupboard]
