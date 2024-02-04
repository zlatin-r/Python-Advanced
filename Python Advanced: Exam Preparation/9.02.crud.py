SIZE = 6

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    matrix.append(input().split())

row, col = list(map(int, input().strip("(").strip(")").split(", ")))

command = input()

while command != "Stop":
    data = command.split(", ")
    action = data[0]
    direction = data[1]

    row += directions[direction][0]
    col += directions[direction][1]

    curr_pos_value = matrix[row][col]

    if action == "Create":
        value = data[2]

        if curr_pos_value == ".":
            matrix[row][col] = value

    elif action == "Update":
        value = data[2]

        if curr_pos_value != ".":
            matrix[row][col] = value

    elif action == "Delete":

        if curr_pos_value != ".":
            matrix[row][col] = "."

    elif action == "Read":

        if curr_pos_value != ".":
            print(matrix[row][col])

    command = input()

[print(*row) for row in matrix]
