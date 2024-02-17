from collections import deque

amount_money = [int(x) for x in input().split()]
prices = deque(int(x) for x in input().split())

eaten_food = 0

while amount_money and prices:

    curr_money = amount_money.pop()
    price = prices.popleft()

    if curr_money == price:
        eaten_food += 1
    elif curr_money > price:

        if amount_money:
            amount_money[-1] += curr_money - price
        eaten_food += 1

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif 1 < eaten_food < 4:
    print(f"Henry ate: {eaten_food} foods.")
elif eaten_food == 1:
    print(f"Henry ate: {eaten_food} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
