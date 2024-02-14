SIZE = int(input())
board = []

start_pos = (0, 0)
money = 100

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for rows in range(SIZE):
    board.append(list(input()))

    if "G" in board[rows]:
        start_pos = rows, board[rows].index("G")
        board[start_pos[0]][start_pos[1]] = "-"

r, c = start_pos

while True:
    command = input()

    if command == "end":
        print(f"End of the game. Total amount: {money}$")
        break

    r += directions[command][0]
    c += directions[command][1]

    if 0 <= r < SIZE and 0 <= c < SIZE:
        symbol = board[r][c]

        if symbol == "W":
            money += 100
        elif symbol == "P":
            money -= 200
        elif symbol == "J":
            money += 100000
            print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
            break

        if money <= 0:
            print("Game over! You lost everything!")
            break

        board[r][c] = "-"

    else:
        money = 0
        print("Game over! You lost everything!")
        break

board[r][c] = "G"

if money > 0:
    [print("".join(row)) for row in board]
