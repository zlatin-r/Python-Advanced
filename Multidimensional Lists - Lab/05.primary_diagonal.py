n = int(input())

matrix = []
diagonal_sum = 0

for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
