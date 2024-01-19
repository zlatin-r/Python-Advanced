rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sub_matrix = []
max_sum = float('-inf')

for row in range(rows - 2):
    for col in range(columns - 2):

        up_left = matrix[row][col]
        up_mid = matrix[row][col + 1]
        up_right = matrix[row][col + 2]
        mid_left = matrix[row + 1][col]
        mid_mid = matrix[row + 1][col + 1]
        mid_right = matrix[row + 1][col + 2]
        down_left = matrix[row + 2][col]
        down_mid = matrix[row + 2][col + 1]
        down_right = matrix[row + 2][col + 2]

        sub_matrix_sum = (up_left + up_mid + up_right +
                          mid_left + mid_mid + mid_right +
                          down_left + down_mid + down_right)

        if sub_matrix_sum > max_sum:
            max_sum = sub_matrix_sum
            sub_matrix = [[up_left, up_mid, up_right],
                          [mid_left, mid_mid, mid_right],
                          [down_left, down_mid, down_right]]

print(f"Sum = {max_sum}")
for row in sub_matrix:
    print(*row)
