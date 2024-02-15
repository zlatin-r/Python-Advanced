from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

total_worms = len(worms)
matches = 0

while worms and holes:
    curr_worm = worms.pop()
    curr_hole = holes.popleft()

    if curr_worm == curr_hole:
        matches += 1
    else:
        curr_worm -= 3

        if curr_worm > 0:
            worms.append(curr_worm)

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if total_worms == matches:
    print("Every worm found a suitable hole!")
elif not worms and matches < total_worms:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(map(str, worms))}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")
