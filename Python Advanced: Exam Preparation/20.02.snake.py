SIZE = int(input())
field = []

eaten_food = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

r, c = 0, 0
burrow_one, burrow_two = [0, 0], [0, 0]

for rows in range(SIZE):
    field.append(list(input()))

    if "S" in field[rows]:
        r, c = rows, field[rows].index("S")
        field[r][c] = "."

while True:
    command = input()

    r += directions[command][0]
    c += directions[command][1]

    if 0 <= r < SIZE and 0 <= c < SIZE:

        current_pos = field[r][c]

        if current_pos == "*":
            eaten_food += 1

        elif current_pos == "B":

            for row in range(SIZE):
                for col in range(SIZE):

                    if field[row][col] == "B":
                        r = row
                        c = col
                    field[r][c] = "."

        field[r][c] = "."
    else:
        print("Game over!")
        break

    if eaten_food == 10:
        print("You won! You fed the snake.")
        field[r][c] = "S"
        break

print(f"Food eaten: {eaten_food}")
[print(''.join(row)) for row in field]
