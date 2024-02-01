SIZE = int(input())

battle_field = []
cruisers = 3
submarine_damage = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    battle_field.append(list(input()))

    if "S" in battle_field[row]:
        r, c = row, battle_field[row].index("S")
        battle_field[r][c] = "-"

command = input()

while True:

    r += directions[command][0]
    c += directions[command][1]
    symbol = battle_field[r][c]

    if symbol == "*":
        submarine_damage += 1

        if submarine_damage == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
            break

    elif symbol == "C":
        cruisers -= 1

        if cruisers == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    battle_field[r][c] = "-"

    command = input()

battle_field[r][c] = "S"
[print(''.join(row)) for row in battle_field]
