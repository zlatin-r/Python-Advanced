from collections import deque

operators = ["+", "-", "/", "*"]


def math_operations(*args, **kwargs):

    numbers = deque(args)

    while numbers:

        for k, v in kwargs.items():
            current_number = numbers.popleft()
            kwargs[k] = current_number + v
