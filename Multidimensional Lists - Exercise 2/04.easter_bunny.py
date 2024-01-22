n = int(input())

matrix = []
sub_matrix = []
bunny_position = 0, 0
max_eggs = float('-inf')
best_way = []
best_direction = ""
start = 0, 0

for i in range(n):
    data = input().split()
    if "B" in data:
        start = i, data.index("B")
    matrix.append(data)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for direction in directions.keys():
    bunny_position = start
    bunny_position = [bunny_position[0] + directions[direction][0], bunny_position[1] + directions[direction][1]]
    eggs = 0

    while (matrix[bunny_position[0]][bunny_position[1]] != "X" and
           0 <= bunny_position[0] < n and 0 <= bunny_position[1] < n):

        eggs += int(matrix[bunny_position[0]][bunny_position[1]])
        sub_matrix.append(bunny_position)
        bunny_position = [bunny_position[0] + directions[direction][0], bunny_position[1] + directions[direction][1]]

    if eggs > max_eggs:
        max_eggs = eggs
        best_way = sub_matrix
        best_direction = direction
