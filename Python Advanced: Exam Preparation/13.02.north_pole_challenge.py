def row_col_pos_checker(r, c):
    if r > rows - 1:
        r = 0
    if r < 0:
        r = rows - 1
    if c > columns - 1:
        c = 0
    if c < 0:
        c = columns - 1

    return r, c


rows, columns = map(int, input().split(", "))

field = []
total_items = 0
collected_items = {"D": 0, "G": 0, "C": 0}
all_collected = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    field.append(input().split())

    if "Y" in field[row]:
        row_pos, col_pos = row, field[row].index("Y")
        field[row_pos][col_pos] = "x"

    total_items += field[row].count("D")
    total_items += field[row].count("G")
    total_items += field[row].count("C")

command = input()

while command != "End":
    direction, steps = command.split("-")

    for step in range(int(steps)):

        row_pos += directions[direction][0]
        col_pos += directions[direction][1]

        row_pos, col_pos = row_col_pos_checker(row_pos, col_pos)
        current_position = field[row_pos][col_pos]

        if current_position == "D":
            collected_items["D"] += 1
        elif current_position == "G":
            collected_items["G"] += 1
        elif current_position == "C":
            collected_items["C"] += 1

        if total_items == sum(collected_items.values()):
            print("Merry Christmas!")
            all_collected = True
            break

        field[row_pos][col_pos] = "x"

    if all_collected:
        break

    command = input()

field[row_pos][col_pos] = "Y"

print("You've collected:")
print(f"- {collected_items['D']} Christmas decorations")
print(f"- {collected_items['G']} Gifts")
print(f"- {collected_items['C']} Cookies")

[print(*row) for row in field]
