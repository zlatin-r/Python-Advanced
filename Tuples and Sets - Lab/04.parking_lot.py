n = int(input())
garage = set()


for _ in range(n):
    direction, number = input().split(', ')

    if direction == "IN":
        garage.add(number)
    elif direction == "OUT":
        if number in garage:
            garage.remove(number)


if not garage:
    print("Parking Lot is Empty")
else:
    for num in garage:
        print(num)
