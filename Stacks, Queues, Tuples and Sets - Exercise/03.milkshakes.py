from collections import deque

chocolate = deque(int(x) for x in input().split(", "))
milk = deque(int(x) for x in input().split(", "))

shakes_count = 0

while (chocolate and milk) and shakes_count != 5:
    curr_chocolate = chocolate.pop()
    curr_milk = milk.popleft()

    if curr_chocolate <= 0 and curr_chocolate == curr_milk:
        continue
    elif curr_chocolate <= 0:
        milk.appendleft(curr_milk)
        continue
    elif curr_milk <= 0:
        chocolate.append(curr_chocolate)
        continue
    if curr_chocolate == curr_milk:
        shakes_count += 1
    else:
        milk.append(curr_milk)
        chocolate.append(curr_chocolate - 5)

if shakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print("Chocolate:", ", ".join(map(str, chocolate)))
else:
    print("Chocolate: empty")
if milk:
    print("Milk:", ", ".join(map(str, milk)))
else:
    print("Milk: empty")
