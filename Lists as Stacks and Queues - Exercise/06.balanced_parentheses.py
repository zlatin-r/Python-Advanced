from collections import deque

open_parentheses = "({["
closed_parentheses = ")}]"

sequence = deque(input())
counter = 0

while sequence and counter < len(sequence) / 2:
    if sequence[0] not in open_parentheses:
        break
    index = open_parentheses.index(sequence[0])
    if sequence[1] == closed_parentheses[index]:
        sequence.popleft()
        sequence.popleft()
        sequence.rotate(counter)
        counter = 0
    else:
        sequence.rotate(-1)
        counter += 1

if sequence:
    print("NO")
else:
    print("YES")