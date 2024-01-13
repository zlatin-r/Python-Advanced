from collections import deque

cups = deque(int(x) for x in input(). split())
bottles = deque(int(x) for x in input(). split())
wasted_water = 0

while bottles and cups:
    current_bottle = bottles.pop()

    if cups[0] <= current_bottle:
        wasted_water += current_bottle - cups[0]
        cups.popleft()
    else:
        cups[0] -= current_bottle

if cups:
    print("Cups:", *cups)
else:
    print("Bottles:", *bottles)
print(f"Wasted litters of water: {wasted_water}")
