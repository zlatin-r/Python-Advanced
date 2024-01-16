from collections import deque

chocolate = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

shakes_count = 0

while chocolate and cups_of_milk:

    if chocolate[-1] <= 0:
        current_chocolate = chocolate.pop()
        if len(chocolate) == 0:
            print("Not enough milkshakes.")
            break

    if cups_of_milk[0] <= 0:
        current_cups_of_milk = cups_of_milk.popleft()
        if len(cups_of_milk) == 0:
            print("Not enough milkshakes.")
            break

    current_chocolate = chocolate.pop()
    current_cups_of_milk = cups_of_milk.popleft()

    if current_chocolate == current_cups_of_milk:
        shakes_count += 1
        if shakes_count == 5:
            print("Great! You made all the chocolate milkshakes needed!")
            break
    else:
        cups_of_milk.append(current_cups_of_milk)
        chocolate.append(current_chocolate - 5)

if len(chocolate) > 0:
    print("Chocolate:", ", ".join(map(str, chocolate)))
else:
    print("Chocolate: empty")

if len(cups_of_milk) > 0:
    print("Milk:", ", ".join(map(str, cups_of_milk)))
else:
    print("Milk: empty")
