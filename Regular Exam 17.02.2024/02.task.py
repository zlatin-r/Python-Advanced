SIZE = int(input())

airspace = []
r, c = (0, 0)

armor = 300
enemies = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    airspace.append(list(input()))

    if "J" in airspace[row]:
        r, c = row, airspace[row].index("J")
        airspace[r][c] = "-"

    if "E" in airspace[row]:
        enemies += airspace[row].count("E")

while enemies and armor:
    command = input()

    r += directions[command][0]
    c += directions[command][1]

    curr_symbol = airspace[r][c]

    if curr_symbol == "E":
        enemies -= 1

        if enemies:
            armor -= 100

    elif curr_symbol == "R":
        armor = 300

    airspace[r][c] = "-"

airspace[r][c] = "J"

if not enemies:
    print("Mission accomplished, you neutralized the aerial threat!")
elif not armor:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")

[print("".join(row)) for row in airspace]
