first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    command = input().split()

    action = " ".join(command[0:2])
    numbers = [int(x) for x in command[2:]]

    if action == "Add First":
        for x in numbers:
            first_sequence.add(x)  # [first_set.add(x) for x in numbers]
    elif action == "Add Second":
        for x in numbers:
            second_sequence.add(x)
    elif action == "Remove First":
        first_sequence = first_sequence.difference(numbers)
    elif action == "Remove Second":
        second_sequence = second_sequence.difference(numbers)
    elif action == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
