SIZE = int(input())
moves = input().split(", ")

field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

hazelnuts = 0
print_message = True

for row in range(SIZE):
    field.append(list(input()))

    if "s" in field[row]:
        r, c = row, field[row].index("s")

for direction in moves:

    r += directions[direction][0]
    c += directions[direction][1]

    if 0 <= r < SIZE and 0 <= c < SIZE:
        curr_symbol = field[r][c]

        if curr_symbol == "h":
            field[r][c] = "*"
            hazelnuts += 1

            if hazelnuts == 3:
                print("Good job! You have collected all hazelnuts!")
                print_message = False
                break

        elif curr_symbol == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            print_message = False
            break

    else:
        print("The squirrel is out of the field.")
        print_message = False
        break

if print_message:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
