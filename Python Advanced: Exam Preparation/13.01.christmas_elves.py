from collections import deque

elves_energy = deque(int(x) for x in input().split())
material_boxes = [int(x) for x in input().split()]

box = 0
total_toys = 0
total_energy = 0

while elves_energy and material_boxes:

    current_evl_energy = elves_energy.popleft()
    current_material_box = material_boxes.pop()

    box += 1

    if box % 3 == 0:
        current_material_box *= 2

        if current_material_box > current_evl_energy:
            current_material_box /= 2

    if current_evl_energy >= current_material_box:
        current_evl_energy -= current_material_box
        total_energy += current_material_box

        if box % 5 == 0:
            elves_energy.append(current_evl_energy)
            continue

        current_evl_energy += 1
        elves_energy.append(current_evl_energy)

        if box % 3 == 0:
            total_toys += 2
        else:
            total_toys += 1
    else:
        material_boxes.append(current_material_box)
        current_evl_energy *= 2
        elves_energy.append(current_evl_energy)

print(f"Toys: {total_toys}")
print(f"Energy: {int(total_energy)}")
print(f"Elves left: {', '.join(str(x) for x in elves_energy)}")
