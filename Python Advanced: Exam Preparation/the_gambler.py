SIZE = int(input())

money = 100
gambler_pos = []
end_game = False

board = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    board.append(list(input()))

    if "G" in board[row]:
        gambler_pos = row, board[row].index("G")
        board[gambler_pos[0]][gambler_pos[1]] = "-"

command = input()
while command != "end":
    gambler_pos = gambler_pos[0] + directions[command][0], gambler_pos[1] + directions[command][1]

    if 0 <= gambler_pos[0] < SIZE and 0 <= gambler_pos[1] < SIZE:
        symbol = board[gambler_pos[0]][gambler_pos[1]]

        if symbol == "W":
            money += 100
        elif symbol == "P":
            money -= 200
        elif symbol == "J":
            money += 100000
            print("You win the Jackpot!")
            break

        if money <= 0:
            print("Game over! You lost everything!")
            break
    else:
        money = 0
        print("Game over! You lost everything!")

    board[gambler_pos[0]][gambler_pos[1]] = "-"
    command = input()

board[gambler_pos[0]][gambler_pos[1]] = "G"
if money > 0:
    print(f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in board]
