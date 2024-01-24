SIZE = int(input())
directions_data = input().split()

matrix = []
miner_pos = []

total_coal = 0
collected_coal = 0
count = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = row, matrix[row].index("s")
    total_coal += matrix[row].count("c")

r = miner_pos[0]
c = miner_pos[1]

for direction in directions_data:
    count += 1

    r += directions[direction][0]
    c += directions[direction][1]

    if 0 <= r < SIZE and 0 <= c < SIZE:
        symbol = matrix[r][c]

        if symbol == "c":
            collected_coal += 1
            matrix[r][c] = "*"
        elif symbol == "e":
            print("Game over!", (r, c))
            break

        if total_coal == collected_coal:
            print("You collected all coal!", (r, c))
            break

        if count == len(directions_data) and total_coal > collected_coal:
            print(f"{total_coal - collected_coal} pieces of coal left.", (r, c))
            break

    else:
        r -= directions[direction][0]
        c -= directions[direction][1]
