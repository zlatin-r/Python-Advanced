n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])

for j in range(len(matrix)):
    secondary_diagonal.append(matrix[j][n - 1])
    n -= 1

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
