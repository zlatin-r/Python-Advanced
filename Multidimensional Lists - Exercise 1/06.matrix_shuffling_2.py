rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

valid_rows = range(rows)
valid_columns = range(columns)

command = input()

while command != "END":
    command = command.split()
    action = command[0]
    data = [int(x) for x in command[1:] if x.isnumeric()]

    if ((action != "swap" or
            len(data) != 4 or
            not {data[0], data[2]}.issubset(valid_rows)) or
            not {data[1], data[2]}.issubset(valid_columns)):
        print("Invalid input!")
    else:
        matrix[data[0]][data[1]], matrix[data[2]][data[3]] = matrix[data[2]][data[3]], matrix[data[0]][data[1]]

        [print(*row) for row in matrix]

    command = input()
