from collections import deque

stations = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

index = 0
gas_in_tank = 0
stations_copy = stations.copy()

while stations_copy:
    gas, distance = stations_copy.popleft()
    gas_in_tank += gas

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        stations.rotate(-1)
        stations_copy = stations.copy()
        index += 1
        gas_in_tank = 0

print(index)
