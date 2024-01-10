expression = input()
stack = list()

for char in range(len(expression)):
    if expression[char] == "(":
        stack.append(char)
    elif expression[char] == ")":
        start_index = stack.pop()
        print(expression[start_index:char + 1])
