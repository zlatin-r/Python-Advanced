from collections import deque

orders = deque(int(x) for x in input().split(", "))
employees = [int(x) for x in input().split(", ")]

total_pizzas = 0

while orders and employees:

    order = orders.popleft()
    employee_capacity = employees.pop()

    if order <= 0:
        employees.append(employee_capacity)
        continue

    if order > 10:
        employees.append(employee_capacity)
        continue

    if order <= employee_capacity:
        total_pizzas += order
    else:
        order -= employee_capacity
        total_pizzas += order
        orders.appendleft(order)

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(map(str, employees))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, orders))}")