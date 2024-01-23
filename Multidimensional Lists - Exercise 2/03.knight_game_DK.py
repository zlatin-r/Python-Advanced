size = int(input())
matrix = [list(input()) for _ in range(size)]

removed_knights = 0

moves = (
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
    max_attack = 0
    max_attack_knight_pos = []

    for row in range(size):
        for col in range(size):

            if matrix[row][col] == "K":
                attack = 0

                for move in moves:
                    r = row + move[0]
                    c = col + move[1]

                    if 0 <= r < size and 0 <= c < size:
                        if matrix[r][c] == "K":
                            attack += 1

                if attack > max_attack:
                    max_attack_knight_pos = [row, col]
                    max_attack = attack

    if max_attack_knight_pos:
        r, c = max_attack_knight_pos
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
