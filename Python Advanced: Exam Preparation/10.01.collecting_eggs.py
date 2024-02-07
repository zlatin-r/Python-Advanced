from collections import deque

filled_boxes = 0

eggs_sizes = deque(int(x) for x in input().split(", "))
paper_sizes = [int(x) for x in input().split(", ")]

while eggs_sizes and paper_sizes:

    curr_egg_size = eggs_sizes.popleft()
    curr_paper_size = paper_sizes.pop()

    if curr_egg_size > 0 and curr_egg_size != 13:
        if curr_egg_size + curr_paper_size <= 50:
            filled_boxes += 1
    elif curr_egg_size == 13:
        paper_sizes.append(curr_paper_size)
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
    else:
        paper_sizes.append(curr_paper_size)

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_sizes)}")

if paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sizes)}")
