SIZE = int(input())

fishing_area = []
r, c = [0, 0]
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
        r, c = row, fishing_area[row].index("S")
        fishing_area[r][c] = "-"

command = input()
while command != "collect the nets":

    r += directions[command][0]
    c += directions[command][1]

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        r = (r % SIZE)
        c = (c % SIZE)

    if fishing_area[r][c].isdigit():
        collected_fish += int(fishing_area[r][c])
    elif fishing_area[r][c] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{r},{c}]")
        exit()

    fishing_area[r][c] = "-"
    command = input()

fishing_area[r][c] = "S"

if collected_fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    fish_needed = 20 - collected_fish
    print(f"You didn't catch enough fish and didn't reach the quota! You need {fish_needed} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print("".join(row)) for row in fishing_area]
