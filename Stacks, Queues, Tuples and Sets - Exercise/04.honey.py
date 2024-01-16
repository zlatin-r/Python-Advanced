from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

collected_honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
        continue

    current_symbol = symbols.popleft()
    if current_nectar > 0:
        collected_honey += abs(eval(f"{current_bee} {current_symbol} {current_nectar}"))

print(f"Total honey made: {collected_honey}")

if bees:
    print("Bees left:", ", ".join(map(str, bees)))
if nectar:
    print("Nectar left:", ", ".join(map(str, nectar)))
