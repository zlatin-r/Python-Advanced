presents_count = int(input())
SIZE = int(input())

neighborhood = []
santa_pos = []
total_nice_kids = 0
nice_kids_received_gifts = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    neighborhood.append(input().split())

    if "S" in neighborhood[row]:
        santa_pos = [row, neighborhood[row].index("S")]

    if "V " in neighborhood[row] or "X " in neighborhood[row]:
        total_nice_kids += neighborhood[row].index("V")

direction = input()
while presents_count and direction != "Christmas morning":
    santa_pos[0] += directions[direction][0]
    santa_pos[1] += directions[direction][1]

    if 0 <= santa_pos[0] < SIZE and 0 <= santa_pos[1] < SIZE:
        symbol = neighborhood[santa_pos[0]][santa_pos[1]]

        if symbol == "V":
            nice_kids_received_gifts += 1
            presents_count -= 1

        elif symbol == "C":
            neighborhood[santa_pos[0]][santa_pos[1]] = "-"
            for pos in directions.values():
                r = santa_pos[0] + pos[0]
                c = santa_pos[1] + pos[1]

                if neighborhood[r][c].isalpha():
                    if neighborhood[r][c] == "V":
                        nice_kids_received_gifts += 1

                    neighborhood[r][c] = "-"
                    presents_count -= 1

                if not presents_count:
                    break
            if not presents_count:
                break
        neighborhood[santa_pos[0]][santa_pos[1]] = "-"
    direction = input()

if presents_count and total_nice_kids > nice_kids_received_gifts:
    print("Santa ran out of presents!")
    [print(*row) for row in neighborhood]
    print(f"No presents for {total_nice_kids - nice_kids_received_gifts} nice kid/s.")
else:
    [print(*row) for row in neighborhood]
    print(f"Good job, Santa! {nice_kids_received_gifts} happy nice kid/s.")

