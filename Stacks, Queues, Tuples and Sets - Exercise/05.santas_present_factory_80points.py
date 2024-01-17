from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents = {"Doll": 150, "Wooden train": 250,
            "Teddy bear": 300, "Bicycle": 400}

crafted_toys = {}
success = False

while materials and magic:
    curr_material = materials.pop()
    curr_magic = magic.popleft()

    magic_level = curr_material * curr_magic

    if magic_level in presents.values():
        for key, value in presents.items():
            if value == magic_level:
                if key in crafted_toys.keys():
                    crafted_toys[key] += 1
                    continue
                crafted_toys[key] = 1
    elif magic_level < 0:
        materials.append(curr_material + curr_magic)
    elif magic_level > 0:
        curr_material += 15
        materials.append(curr_material)
    else:
        if curr_material == 0 and curr_magic == 0:
            continue
        elif curr_material == 0:
            magic.appendleft(curr_magic)
        elif curr_magic == 0:
            materials.append(curr_material)

    if ("Doll" in crafted_toys.keys() and
        "Wooden train" in crafted_toys.keys()) or (
            "Teddy bear" in crafted_toys.keys() and
            "Bicycle" in crafted_toys.keys()):
        success = True

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left:", ", ".join(map(str, materials[::-1])))

if magic:
    print("Magic left:", ", ".join(map(str, magic)))

for toy, num in sorted(crafted_toys.items()):
    print(f"{toy}: {num}")
