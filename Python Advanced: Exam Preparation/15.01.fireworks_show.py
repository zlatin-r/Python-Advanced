from collections import deque

effects = deque(int(x) for x in input().split(', '))
explosive_power = [int(x) for x in input().split(', ')]

fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

while effects and explosive_power:

    effect = effects.popleft()
    power = explosive_power.pop()

    if effect <= 0:
        explosive_power.append(power)
        continue
    if power <= 0:
        effects.appendleft(effect)
        continue

    result = effect + power

    if result % 3 == 0 and result % 5 != 0:
        fireworks["Palm Fireworks"] += 1
    elif result % 5 == 0 and result % 3 != 0:
        fireworks["Willow Fireworks"] += 1
    elif result % 3 == 0 and result % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    else:
        effect -= 1
        effects.append(effect)
        explosive_power.append(power)

if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
