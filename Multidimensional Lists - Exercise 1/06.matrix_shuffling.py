rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    command = command.split()
    action = command[0]
    data = [int(x) for x in command[1:] if x.isnumeric()]

    if action != "swap" or len(data) != 4:
        print("Invalid input!")
    elif ((data[0] > rows or
          data[1] > columns or
          data[2] > rows or
          data[3] > columns) or
          (data[0] < 0 or
           data[1] < 0 or
           data[2] < 0 or
           data[3] < 0)):
        print("Invalid input!")
    else:
        from_row, from_col = data[0], data[1]
        to_row, to_col = data[2], data[3]

        matrix[from_row][from_col], matrix[to_row][to_col] = matrix[to_row][to_col], matrix[from_row][from_col]

        [print(*row) for row in matrix]

    command = input()
