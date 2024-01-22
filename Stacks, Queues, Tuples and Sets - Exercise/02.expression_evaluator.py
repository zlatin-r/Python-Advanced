from collections import deque

str_expression = deque(input().split())
operators = "*/+-"
meet_numbers = []
result = 0

for el in range(len(str_expression)):
    current_el = str_expression.popleft()

    if current_el not in operators:
        meet_numbers.append(int(current_el))
    else:
        result = meet_numbers[0]

        if current_el == "+":
            result = sum(meet_numbers)
        elif current_el == "-":
            for num in meet_numbers[1:]:
                result -= num
        elif current_el == "*":
            for num in meet_numbers[1:]:
                result *= num
        elif current_el == "/":
            for num in meet_numbers[1:]:
                result /= num
            result = int(result)

        meet_numbers = [result]

print(result)
