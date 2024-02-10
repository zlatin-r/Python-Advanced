from collections import deque

materials = [int(x) for x in input().split()]
magic_level_values = deque(int(x) for x in input().split())

gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while materials and magic_level_values:

    material = materials.pop()
    magic_level = magic_level_values.popleft()

    result = material + magic_level

    if result < 100 and result % 2 == 0:
        material *= 2
        magic_level *= 3
        result = material + magic_level
    elif result < 100 and result % 2 == 1:
        result *= 2
    elif result > 499:
        result /= 2

    if 100 <= result <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= result <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= result <= 399:
        gifts["Gold"] += 1
    elif 400 <= result <= 499:
        gifts["Diamond Jewellery"] += 1

if (gifts["Gemstone"] and gifts["Porcelain Sculpture"]) or (gifts["Gold"] and gifts["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level_values:
    print(f"Magic left: {', '.join(map(str, magic_level_values))}")

for key, value in sorted(gifts.items(), key=lambda x: x[0]):
    if value > 0:
        print(f"{key}: {value}")