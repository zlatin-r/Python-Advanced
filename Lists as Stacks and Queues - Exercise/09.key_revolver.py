from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
total_value = int(input())

bullets_count = 0
barrel_load = barrel_size

while bullets and locks:
    bullets_count += 1
    current_bullet = bullets.pop()

    if current_bullet <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print("Ping!")

    barrel_load -= 1
    if barrel_load == 0 and bullets:
        print("Reloading!")
        barrel_load = barrel_size

if not locks:
    earned_money = total_value - (bullets_count * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
