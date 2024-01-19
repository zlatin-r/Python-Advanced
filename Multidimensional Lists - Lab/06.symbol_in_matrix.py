n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(input()))
symbol = input()

for j in matrix:
    if symbol in j:
        print(f"({matrix.index(j)}, {j.index(symbol)})")
        break
else:
    print(f"{symbol} does not occur in the matrix")
