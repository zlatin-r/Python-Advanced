from collections import deque

SIZE = 7
dartboard = []

players_names = deque(input().split(", "))
points = {players_names[0]: 501, players_names[1]: 501}
turns = {players_names[0]: 0, players_names[1]: 0}
bullseye = False

for row in range(SIZE):
    dartboard.append(input().split())

while True:
    r, c = map(int, input().strip("(").strip(")").split(', '))
    current_target = dartboard[r][c]

    player = players_names[0]
    turns[player] += 1

    if 0 <= r < SIZE and 0 <= c < SIZE:
        bonus_sum = int(dartboard[r][0]) + int(dartboard[r][6]) + int(dartboard[0][c]) + int(dartboard[6][c])

        if current_target.isdigit():
            points[player] -= int(current_target)
        elif current_target == "D":
            points[player] -= (bonus_sum * 2)
        elif current_target == "T":
            points[player] -= (bonus_sum * 3)
        elif current_target == "B":
            bullseye = True

        if points[player] <= 0 or bullseye:
            print(f"{player} won the game with {turns[player]} throws!")
            break

    players_names.rotate(1)
