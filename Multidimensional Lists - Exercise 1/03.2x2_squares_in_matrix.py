rows, columns = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
counter = 0

for row in range(rows - 1):
    for col in range(columns - 1):

        up_left = matrix[row][col]
        up_right = matrix[row][col + 1]
        down_left = matrix[row + 1][col]
        down_right = matrix[row + 1][col + 1]

        if up_left == down_left == up_right == down_right:
            counter += 1

print(counter)
