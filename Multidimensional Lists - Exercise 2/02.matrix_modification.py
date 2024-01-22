def valid_check(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    print("Invalid coordinates")


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
cols = len(matrix[0])

command = input()

while command != "END":
    command = command.split()
    action, idx, value = command[0], [int(x) for x in command[1:3]], int(command[3])

    if valid_check(idx[0], idx[1]):
        if action == "Add":
            matrix[idx[0]][idx[1]] += value
        elif action == "Subtract":
            matrix[idx[0]][idx[1]] -= value

    command = input()

[print(*row) for row in matrix]
