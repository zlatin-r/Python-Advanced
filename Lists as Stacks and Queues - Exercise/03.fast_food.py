from collections import deque

food_quantity = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()
    else:
        break

if len(orders) > 0:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print(f"Orders complete")
