rows = int(input())

matrix = []

for i in range(rows):
    row = [int(x) for x in input().split(",") if int(x) % 2 == 0]
    matrix.append(row)

print(matrix)
