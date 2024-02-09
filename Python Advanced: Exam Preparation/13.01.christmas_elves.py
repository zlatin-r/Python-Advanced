from collections import deque

elves_energy = deque(int(x) for x in input().split())
material_boxes = [int(x) for x in input().split()]

total_toys = 0

current_evl = elves_energy.popleft()
current_box = material_boxes.pop()

