SIZE = int(input())
matrix = [list(input()) for _ in range(SIZE)]

removed_knights = 0

directions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2)
)

while True:
    max_attacks_pos = []
    max_attacks = 0

    for row in range(SIZE):
        for col in range(SIZE):
            if matrix[row][col] == "K":
                attack_possibilities = 0

                for direction in directions:
                    r = row + direction[0]
                    c = col + direction[1]

                    if 0 <= r < SIZE and 0 <= c < SIZE:
                        if matrix[r][c] == "K":
                            attack_possibilities += 1

                if attack_possibilities > max_attacks:
                    max_attacks_pos = [row, col]
                    max_attacks = attack_possibilities

    if max_attacks_pos:
        matrix[max_attacks_pos[0]][max_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
