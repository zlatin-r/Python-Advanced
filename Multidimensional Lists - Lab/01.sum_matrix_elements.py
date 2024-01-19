rows, cols = (int(x) for x in input().split(", "))

matrix = []
numbers_sum = 0

for i in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    numbers_sum += sum(row)

print(numbers_sum)
print(matrix)
