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

    if magic_level < 0:
        materials.append(curr_material + curr_magic)
    elif magic_level > 0:
        curr_material += 15
        materials.append(curr_material)
    elif magic_level in presents.values():
        for key, value in presents:
            if value == magic_level:
                crafted_toys[key] += 1

    if ("Doll" in crafted_toys.keys() and
        "Wooden train" in crafted_toys.keys()) or (
            "Teddy bear" in crafted_toys.keys() and
            "Bicycle" in crafted_toys.keys()):
        success = True
        break

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print("Materials left:", ", ".join(map(str, materials)))
if magic:
    print("Magic left:", ", ".join(map(str, magic)))
for toy, num in crafted_toys.items():
    print(f"{toy}: {num}")
