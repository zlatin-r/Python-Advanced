from collections import deque

jobs = deque(int(x) for x in input().split(", "))
task = jobs[int(input())]

total_cycles = 0

while task in jobs:
    start = min(jobs)
    min_el_index = jobs.index(start)

    while jobs.index(start) != 0:
        jobs.rotate(1)
    else:
        total_cycles += jobs.popleft()

print(total_cycles)
