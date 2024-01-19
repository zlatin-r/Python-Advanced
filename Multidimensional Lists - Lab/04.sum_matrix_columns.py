rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for col_index in range(columns):
    sum_col = 0
    for row_index in range(rows):
        el = matrix[row_index][col_index]
        sum_col += matrix[row_index][col_index]
    print(sum_col)
