word = input()

SIZE = int(input())
filed = []

start_pos = (0, 0)

for row in range(SIZE):
    filed.append(input().split())

    if "P" in filed[row]:
        start_pos = row, filed[row].index("P")

r, c = start_pos[0], start_pos[1]
filed[r][c] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

commands = int(input())

for _ in range(commands):
    r, c = directions[input()]

    if 0 <= r < SIZE and 0 <= c < SIZE:
        symbol = filed[r][c]

        if symbol.isalpha():
            word += symbol
            filed[r][c] = "-"

    else:
        word = word[:-1]

print(word)
