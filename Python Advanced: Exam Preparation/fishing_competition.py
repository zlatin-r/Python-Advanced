SIZE = int(input())

fishing_area = []
ship_pos = []
collected_fish = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    fishing_area.append(list(input()))

    if "S" in fishing_area[row]:
        ship_pos = row, fishing_area[row].index("S")
        fishing_area[ship_pos[0]][ship_pos[1]] = "-"

command = input()
while command != "collect the nets":
    r, c = [
        ship_pos[0] + directions[command][0],
        ship_pos[1] + directions[command][1]
    ]

    if r >= SIZE:
        r = 0
    elif r < 0:
        r = SIZE - 1
    elif c >= SIZE:
        c = 0
    elif c < 0:
        c = SIZE - 1

    if fishing_area[r][c].isdigit():
        collected_fish += int(fishing_area[r][c])
    elif fishing_area[r][c] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{r},{c}]")
        exit()

    fishing_area[r][c] = "-"

    ship_pos = r, c
    command = input()

fishing_area[ship_pos[0]][ship_pos[1]] = "S"

if collected_fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    fish_needed = 20 - collected_fish
    print(f"You didn't catch enough fish and didn't reach the quota! You need {fish_needed} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print("".join(row)) for row in fishing_area]
