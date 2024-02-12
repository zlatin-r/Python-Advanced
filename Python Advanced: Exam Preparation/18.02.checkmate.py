SIZE = 8
board = []
capture_coordinates = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for rows in range(SIZE):
    board.append(input().split())

for r in range(SIZE):
    for c in range(SIZE):
        current_pos = board[r][c]

        if current_pos == "Q":
            for direction in directions:
                while board[r][c] != "K" or 0 <= r < SIZE and 0 <= c < SIZE:
                    r += direction[0]
                    c += direction[1]
                else:
                    capture_coordinates.append([r, c])
