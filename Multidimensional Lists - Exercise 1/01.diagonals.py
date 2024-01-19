n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])
    #  matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    #  primary_diagonal = [matrix[i][i] for i in range(n)]

for j in range(len(matrix)):
    secondary_diagonal.append(matrix[j][n - 1])
    n -= 1
    #  secondary_diagonal = [matrix[j][n - j - 1] for j in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
