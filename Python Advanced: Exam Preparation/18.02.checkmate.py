SIZE = 8
board = []
capture_coordinates = []
king_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_left": (1, -1),
    "down_right": (1, 1)
}

for rows in range(SIZE):
    board.append(input().split())

    if "K" in board[rows]:
        king_pos = [rows, board[rows].index("K")]

r, c = king_pos


for direction in directions:
    while True:
        r += directions[direction][0]
        c += directions[direction][1]

        if 0 <= r < SIZE and 0 <= c < SIZE:
            if board[r][c] == "Q":
                capture_coordinates.append([r, c])
                r, c = king_pos
                break
        else:
            r, c = king_pos
            break

if capture_coordinates:
    print(*capture_coordinates, sep="\n")
else:
    print("The king is safe!")
