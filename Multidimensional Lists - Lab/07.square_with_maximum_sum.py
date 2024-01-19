rows, columns = [int(x) for x in input().split(", ")]

matrix = []
max_sum = float("-inf")
sub_matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

for row_idx in range(rows - 1):
    for col_idx in range(columns - 1):
        curr_sum = 0

        up_left = matrix[row_idx][col_idx]
        up_right = matrix[row_idx][col_idx + 1]
        down_left = matrix[row_idx + 1][col_idx]
        down_right = matrix[row_idx + 1][col_idx + 1]

        curr_sum += up_left + up_right + down_left + down_right
        if curr_sum > max_sum:
            max_sum = curr_sum
            sub_matrix = []
            sub_matrix.append([up_left, up_right])
            sub_matrix.append([down_left, down_right])

for row in sub_matrix:
    print(*row)
print(max_sum)
