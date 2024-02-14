from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

matches = 0
all_fit = True

while worms and holes:

    if worms[-1] == holes[0]:
        matches += 1
        worms.pop()
        holes.popleft()
    else:
        holes.popleft()
        worms[-1] -= 3

        if worms[-1] <= 0:
            worms.pop()
            all_fit = False

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and all_fit:
    print("Every worm found a suitable hole!")
elif not worms and not all_fit:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(map(str, worms))}")

if holes:
    print(f"Holes left: {', '.join(map(str, holes))}")
else:
    print("Holes left: none")
