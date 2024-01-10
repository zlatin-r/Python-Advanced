from collections import deque

people = deque()
quantity = int(input())
name = input()

while name != "Start":
    people.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if data[0] == "refill":
        quantity = int(data[1])
    else:
        if quantity >= int(data[0]):
            quantity -= int(data[0])
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    command = input()
print(f"{quantity} liters left")
