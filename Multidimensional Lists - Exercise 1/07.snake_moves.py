from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = deque(x for x in input())

matrix = []

for _ in range(rows):
    matrix.append(['*' for _ in range(columns)])

for i in range(rows):
    for j in range(columns):

        curr_snake_el = snake.popleft()
        matrix[i][j] = curr_snake_el
        snake.append(curr_snake_el)

    if i % 2 == 1:
        matrix[i].reverse()

for row in matrix:
    print("".join(row))
