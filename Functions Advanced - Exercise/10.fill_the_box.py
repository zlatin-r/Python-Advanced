from collections import deque


def fill_the_box(*args):

    box_size = args[0] * args[1] * args[2]
    cubes = deque(args[3:])

    while cubes[0] != "Finish":

        box_size -= cubes.popleft()

        if box_size <= 0:
            cubes_left = sum(c for c in cubes if c != "Finish")
            return f"No more free space! You have {cubes_left + abs(box_size)} more cubes."

    return f"There is free space in the box. You could put {box_size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

