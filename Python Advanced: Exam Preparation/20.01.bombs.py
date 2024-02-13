from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
casings = [int(x) for x in input().split(", ")]

bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

while bomb_effects and casings and not all(x >= 3 for x in bombs.values()):

    casing = casings.pop()
    effect = bomb_effects.popleft()

    if effect + casing == 40:
        bombs["Datura Bombs"] += 1
    elif effect + casing == 60:
        bombs["Cherry Bombs"] += 1
    elif effect + casing == 120:
        bombs["Smoke Decoy Bombs"] += 1
    else:
        casing -= 5
        casings.append(casing)
        bomb_effects.appendleft(effect)

if all(x >= 3 for x in bombs.values()):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print("Bomb Casings: empty")

for k, v in sorted(bombs.items()):
    print(f"{k}: {v}")
