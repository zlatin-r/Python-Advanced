def valid_check(r, c):
    if 0 <= r < 8 and 0 <= c < 8:
        return True


board = []
rows = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
cols = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

for row in range(8):
    board.append(input().split())

    if "w" in board[row]:
        wr, wc = row, board[row].index("w")

    if "b" in board[row]:
        br, bc = row, board[row].index("b")

while True:

    if ((valid_check(wr - 1, wc - 1) and board[wr - 1][wc - 1] == "b") or
            (valid_check(wr - 1, wc + 1) and board[wr - 1][wc + 1] == "b")):
        print(f"Game over! White win, capture on {cols[bc]}{rows[br]}.")
        break

    wr += -1

    if wr > 0:
        board[wr][wc] = "w"
    else:
        print(f"Game over! White pawn is promoted to a queen at {cols[wc]}8.")
        break

    if ((valid_check(br + 1, bc + 1) and board[br + 1][bc + 1] == "w") or
            (valid_check(br + 1, bc - 1) and board[br + 1][bc - 1] == "w")):
        print(f"Game over! Black win, capture on {cols[wc]}{rows[wr]}.")
        break

    br += 1

    if br < 7:
        board[br][bc] = "b"
    else:
        print(f"Game over! Black pawn is promoted to a queen at {cols[bc]}1.")
        break
