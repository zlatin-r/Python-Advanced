rows = int(input())

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.extend(row)

print(matrix)
