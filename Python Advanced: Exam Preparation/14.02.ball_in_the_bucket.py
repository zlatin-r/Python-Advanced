SIZE = 6

scored_points = 0
prices = []

board = []

for _ in range(SIZE):
    board.append(input().split())

for throw in range(3):
    coordinates = input().strip("(").strip(")").split(",")
    r = int(coordinates[0])
    c = int(coordinates[1])

    if 0 <= r < SIZE and 0 <= c < SIZE:
        if board[r][c] == "B":
            board[r][c] = 0
            for i in range(SIZE):
                scored_points += int(board[i][c])

if 100 <= scored_points <= 199:
    prices.append("Football")
elif 200 <= scored_points <= 299:
    prices.append("Teddy Bear")
elif 300 <= scored_points:
    prices.append("Lego Construction Set")

if prices:
    print(f"Good job! You scored {scored_points} points, and you've won {prices[0]}.")
else:
    print(f"Sorry! You need {100 - scored_points} points more to win a prize.")
