from collections import deque

elves_energy = deque(int(x) for x in input().split())
material_boxes = [int(x) for x in input().split()]

box = 0
total_toys = 0
total_energy = 0

while elves_energy and material_boxes:

    elf_energy = elves_energy.popleft()
    material_box = material_boxes.pop()

    if elf_energy < 5:
        material_boxes.append(material_box)
        continue

    box += 1

    if box % 3 == 0:
        material_box *= 2

    if elf_energy >= material_box:
        elf_energy -= material_box
        total_energy += material_box

        if box % 5 == 0:
            elves_energy.append(elf_energy)
            continue

        elf_energy += 1
        elves_energy.append(elf_energy)

        if box % 3 == 0:
            total_toys += 2
        else:
            total_toys += 1
    else:
        if box % 3 == 0:
            material_box /= 2
        material_boxes.append(int(material_box))

        elf_energy *= 2
        elves_energy.append(elf_energy)

print(f"Toys: {total_toys}")
print(f"Energy: {int(total_energy)}")

if elves_energy:
    print(f"Elves left: {', '.join(str(x) for x in elves_energy)}")

if material_boxes:
    print(f"Boxes left: {', '.join(str(x) for x in material_boxes)}")
