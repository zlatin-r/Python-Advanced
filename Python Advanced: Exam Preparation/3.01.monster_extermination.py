from collections import deque

monsters_armor = deque(int(x) for x in input().split(","))
striking_impact = [int(x) for x in input().split(",")]

killed_monsters = 0

while monsters_armor and striking_impact:
    curr_monster = monsters_armor.popleft()
    strike_strength = striking_impact.pop()

    if strike_strength >= curr_monster:
        killed_monsters += 1
        diff = strike_strength - curr_monster

        if diff > 0:
            if striking_impact:
                striking_impact[-1] += diff
            else:
                striking_impact.append(diff)

    else:
        curr_monster -= strike_strength
        monsters_armor.append(curr_monster)

if not monsters_armor:
    print("All monsters have been killed!")

if not striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
