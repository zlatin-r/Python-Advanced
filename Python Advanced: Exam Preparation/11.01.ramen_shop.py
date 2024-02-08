from collections import deque

bowls_ramen = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while customers and bowls_ramen:

    current_bow = bowls_ramen.pop()
    current_customer = customers.popleft()

    if current_bow > current_customer:
        current_bow -= current_customer
        bowls_ramen.append(current_bow)
    elif current_customer > current_bow:
        current_customer -= current_bow
        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")

    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_ramen)}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
