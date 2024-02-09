rows, columns = map(int, input().split())

collected_items = []
field = []

for row in range(rows):
    field.append(input().split())

    if "Y" in field[row]:
        start_row, start_col = row, field[row].index("Y")

