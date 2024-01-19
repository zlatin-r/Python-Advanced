rows, columns = [int(x) for x in input().split(", ")]

matrix = []
sub_matrix = []
max_sum = float("-inf")

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row_idx in range(rows - 1):
    for col_idx in range(columns - 1):

        up_left = matrix[row_idx][col_idx]
        up_right = matrix[row_idx][col_idx + 1]
        down_left = matrix[row_idx + 1][col_idx]
        down_right = matrix[row_idx + 1][col_idx + 1]

        curr_sum = up_left + up_right + down_left + down_right

        if curr_sum > max_sum:
            max_sum = curr_sum
            sub_matrix = [[up_left, up_right], [down_left, down_right]]

for row in sub_matrix:
    print(*row)
print(max_sum)
