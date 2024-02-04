from collections import deque

seats = input().split(", ")

taken_seats = []
rotations = 0

first_seq = deque(int(x) for x in input().split(", "))
second_seq = deque(int(x) for x in input().split(", "))

while len(taken_seats) < 3 and rotations < 10:

    rotations += 1

    first_num = first_seq.popleft()
    second_num = second_seq.pop()

    numbers_sum = first_num + second_num
    character = chr(numbers_sum)

    first_combo, second_combo = str(first_num) + character, str(second_num) + character

    if first_combo not in seats and second_combo not in seats:
        first_seq.append(first_num)
        second_seq.appendleft(second_num)
        continue

    if first_combo in seats and first_combo not in taken_seats:
        taken_seats.append(first_combo)
        seats.remove(first_combo)

    if second_combo in seats and second_combo not in taken_seats:
        taken_seats.append(second_combo)
        seats.remove(second_combo)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
