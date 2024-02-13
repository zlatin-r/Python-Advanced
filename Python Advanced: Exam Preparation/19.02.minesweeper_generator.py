SIZE = int(input())
bombs = int(input())

field = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
bombs_coordinates = []

for _ in range(bombs):
    r, c = map(int, (input().strip("(").strip(")").split(", ")))
    field[r][c] = "*"

print(*field, sep="\n")
