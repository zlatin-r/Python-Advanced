player_one, player_two = input().split(", ")

matrix = []
p1_wait = False
p2_wait = False

for row in range(6):
    matrix.append(input().split())

while True:
    player_one_pos = input()

    if not p1_wait:
        r, c = map(int, player_one_pos.strip("(").strip(")").split(", "))
        current_pos = matrix[r][c]

        if current_pos == "E":
            print(f"{player_one} found the Exit and wins the game!")
            break
        elif current_pos == "T":
            print(f"{player_one} is out of the game! The winner is {player_two}.")
            break
        elif current_pos == "W":
            print(f"{player_one} hits a wall and needs to rest.")
            p1_wait = True
    else:
        p1_wait = False

    player_two_pos = input()

    if not p2_wait:
        r, c = map(int, player_two_pos.strip("(").strip(")").split(", "))
        current_pos = matrix[r][c]

        if current_pos == "E":
            print(f"{player_two} found the Exit and wins the game!")
            break
        elif current_pos == "T":
            print(f"{player_two} is out of the game! The winner is {player_one}.")
            break
        elif current_pos == "W":
            print(f"{player_two} hits a wall and needs to rest.")
            p2_wait = True
    else:
        p2_wait = False
