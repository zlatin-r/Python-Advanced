def find_tunnel_exit(matrix):
    for row in range(SIZE):
        for col in range(SIZE):
            if matrix[row][col] == "T":
                return row, col


SIZE = int(input())
racing_num = int(input())

race_route = []
kilometers_passed = 0
r, c = 0, 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    race_route.append(input().split())

while True:
    command = input()

    if command == "End":
        print(f"Racing car {racing_num} DNF.")
        break

    r += directions[command][0]
    c += directions[command][1]

    pos = race_route[r][c]

    if pos == ".":
        kilometers_passed += 10
    elif pos == "T":
        kilometers_passed += 30
        race_route[r][c] = "."
        r, c = find_tunnel_exit(race_route)
        race_route[r][c] = "."
    elif pos == "F":
        kilometers_passed += 10
        print(f"Racing car {racing_num} finished the stage!")
        break

race_route[r][c] = "C"

print(f"Distance covered {kilometers_passed} km.")
[print(''.join(row)) for row in race_route]
