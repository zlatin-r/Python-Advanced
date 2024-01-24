presents_count = int(input())
SIZE = int(input())

neighborhood = []
santa_pos = []
total_nice_kids = 0
nice_kids_visited = 0

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
    total_nice_kids += neighborhood[row].count("V")

direction = input()
while presents_count and direction != "Christmas morning":
    neighborhood[santa_pos[0]][santa_pos[1]] = "-"
    santa_pos = [
        santa_pos[0] + directions[direction][0],
        santa_pos[1] + directions[direction][1]
    ]
    symbol = neighborhood[santa_pos[0]][santa_pos[1]]

    if symbol == "V":
        nice_kids_visited += 1
        presents_count -= 1
    elif symbol == "C":
        for value in directions.values():
            r = santa_pos[0] + value[0]
            c = santa_pos[1] + value[1]

            if 0 <= r < SIZE and 0 <= c < SIZE:
                if neighborhood[r][c].isalpha():
                    if neighborhood[r][c] == "V":
                        nice_kids_visited += 1
                    presents_count -= 1
                    neighborhood[r][c] = "-"

            if not presents_count:
                break

    neighborhood[santa_pos[0]][santa_pos[1]] = "S"
    if not presents_count:
        break
    direction = input()

if not presents_count and total_nice_kids > nice_kids_visited:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood]

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")
