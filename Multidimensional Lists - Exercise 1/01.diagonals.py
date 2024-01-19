n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])

for j in range(len(matrix)):
    diagonal_el = matrix[j][n - 1]
    secondary_diagonal.append(matrix[j][n - 1])
    n -= 1

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
