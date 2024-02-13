from collections import deque


def list_manipulator(nums, *args):
    numbers = deque(nums)
    commands = list(args)

    if commands[0] == "add" and commands[1] == "beginning":
        rest_nums = commands[2:]
        for num in rest_nums[::-1]:
            numbers.appendleft(num)

    elif commands[0] == "add" and commands[1] == "end":
        rest_nums = commands[2:]
        for num in rest_nums:
            numbers.append(num)

    elif commands[0] == "remove" and commands[1] == "beginning":
        if len(commands) > 2:
            for _ in range(commands[2]):
                numbers.popleft()
        else:
            numbers.popleft()

    elif commands[0] == "remove" and commands[1] == "end":
        if len(commands) > 2:
            for _ in range(commands[2]):
                numbers.pop()
        else:
            numbers.pop()

    return [*numbers]


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
