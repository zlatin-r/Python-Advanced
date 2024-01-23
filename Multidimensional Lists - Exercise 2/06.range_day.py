size = 5
matrix = []
current_pos = [0, 0]
total_targets = 0
targets_hit = 0
hit_positions = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        current_pos = row, matrix[row].index("A")

    if "x" in matrix[row]:
        total_targets += matrix[row].count("x")

n = int(input())
for _ in range(n):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])
        r = current_pos[0] + directions[direction][0] * steps
        c = current_pos[1] + directions[direction][1] * steps

        if 0 <= r < size and 0 <= c < size and matrix[r][c] == ".":
            current_pos = r, c

    elif command[0] == "shoot":
        r = current_pos[0] + directions[direction][0]
        c = current_pos[1] + directions[direction][1]

        while 0 <= r < size and 0 <= c < size:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                targets_hit += 1
                hit_positions.append([r, c])
                break

            r += directions[direction][0]
            c += directions[direction][1]

        if targets_hit == total_targets:
            break

if total_targets != targets_hit:
    print(f"Training not completed! {total_targets - targets_hit} targets left.")
else:
    print(f"Training completed! All {total_targets} targets hit.")
[print(x) for x in hit_positions]
