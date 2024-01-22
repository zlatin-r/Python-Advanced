n = int(input())
matrix = [list(input()) for _ in range(n)]

knight_count = 0
knight_position = []
max_attack = 0
counter = 0

moves = {
    "two_up_left": [-2, -1],
    "two_up_right": [-2, 1],
    "one_up_left": [-1, -2],
    "one_up_right": [-1, 2],
    "two_down_left": [2, -1],
    "two_down_right": [2, 1],
    "one_down_left": [1, -2],
    "one_down_right": [1, 2]
}

for row in matrix:
    for column in row:
        if column == "K":
            knight_position = matrix.index(row), column.index("K")

            for r, c in moves.values():
                knight_position[0], knight_position[1] = row + r, column + c

                if 0 <= knight_position[0] < n and 0 <= c < knight_position[1]:
                    counter += 1
                matrix[knight_position[0]][knight_position[1]] = counter
[print(*row) for row in matrix]
print(matrix)
