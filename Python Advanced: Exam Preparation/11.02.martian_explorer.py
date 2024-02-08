matrix = []

water_found = False
metal_found = False
concrete_found = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(6):
    matrix.append(input().split())

    if "E" in matrix[row]:
        r, c = row, matrix[row].index("E")

commands = input().split(", ")

for command in commands:
    r += directions[command][0]
    c += directions[command][1]

    if r >= 6:
        r = 0
    if r < 0:
        r = 5

    if c >= 6:
        c = 0
    if c < 0:
        c = 5

    position_symbol = matrix[r][c]

    if position_symbol == "W":
        print(f"Water deposit found at ({r}, {c})")
        water_found = True
    elif position_symbol == "M":
        print(f"Metal deposit found at ({r}, {c})")
        metal_found = True
    elif position_symbol == "C":
        print(f"Concrete deposit found at ({r}, {c})")
        concrete_found = True
    elif position_symbol == "R":
        print(f"Rover got broken at ({r}, {c})")
        break

if all([water_found, metal_found, concrete_found]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
