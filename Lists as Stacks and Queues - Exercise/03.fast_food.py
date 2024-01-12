from collections import deque

food_quantity = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    order = orders.popleft()
    if food_quantity >= order:
        food_quantity -= order
    else:
        orders.appendleft(order)
        break

if len(orders) > 0:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print(f"Orders complete")
