from collections import deque

caffeine = [int(x) for x in input().split(", ")]
drinks = deque(int(x) for x in input().split(", "))

stamats_caffeine = 0

while drinks and caffeine:
    curr_caffeine = caffeine.pop()
    curr_drink = drinks.popleft()

    caffeine = curr_drink * curr_caffeine

    if caffeine + stamats_caffeine <= 300:
        stamats_caffeine += caffeine
    else:
        drinks.append(curr_drink)
        stamats_caffeine -= 30

        if stamats_caffeine < 0:
            stamats_caffeine = 0

if drinks:
    print(f"Drinks left: {', '.join(map(str, drinks))}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamats_caffeine} mg caffeine.")
