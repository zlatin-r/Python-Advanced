size = int(input())

matrix = []
alice_pos = (0, 0)
collected_tea_bags = 0
went_to_party = True

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_pos = row, matrix[row].index("A")
        matrix[row][matrix[row].index("A")] = "*"

command = input()

while True:
    alice_pos = alice_pos[0] + moves[command][0], alice_pos[1] + moves[command][1]

    if 0 <= alice_pos[0] < size and 0 <= alice_pos[1] < size:

        if matrix[alice_pos[0]][alice_pos[1]].isdigit():
            collected_tea_bags += int(matrix[alice_pos[0]][alice_pos[1]])
            matrix[alice_pos[0]][alice_pos[1]] = "*"
        elif matrix[alice_pos[0]][alice_pos[1]] == "R":
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            went_to_party = False
            break
        else:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
    else:
        went_to_party = False
        break

    if collected_tea_bags >= 10:
        break

    command = input()

if went_to_party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
