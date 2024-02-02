from collections import deque

caffeine = [int(x) for x in input().split(", ")]
drinks = deque(int(x) for x in input().split(", "))

max_caffeine = 300
total_caffeine = 0

while drinks and caffeine:
    curr_caffeine = caffeine.pop()
    curr_drink = drinks.popleft()

    result = curr_drink * curr_caffeine

    if result <= max_caffeine:
        max_caffeine -= result
        total_caffeine += result
    elif result > max_caffeine:
        drinks.append(curr_drink)
        total_caffeine -= 30
        max_caffeine += 30

        if max_caffeine < 0:
            max_caffeine = 0

if drinks:
    print(f"Drinks left: {', '.join(map(str, drinks))}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
