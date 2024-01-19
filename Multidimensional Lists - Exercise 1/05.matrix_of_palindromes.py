rows, columns = [int(x) for x in input().split()]

matrix = []

for row_idx in range(rows):
    row = []

    for col_idx in range(row_idx, columns):
        row.append(chr(row_idx + 97) + chr(col_idx + 97) + chr(row_idx + 97))

    matrix.append(row)
    columns += 1

[print(*i) for i in matrix]
