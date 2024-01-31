from collections import deque

fuel = [int(x) for x in input().split()]
consumption = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

reached_altitudes = []

for i in range(1, 5):

    current_fuel = fuel.pop()
    current_consumption = consumption.popleft()
    current_fuel_needed = fuel_needed.popleft()

    if current_fuel - current_consumption >= current_fuel_needed:
        print(f"John has reached: Altitude {i}")
        reached_altitudes.append(f"Altitude {i}")
    else:
        print(f"John did not reach: Altitude {i}")
        break

if not fuel_needed:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitudes)}" if reached_altitudes
          else "John didn't reach any altitude.")
