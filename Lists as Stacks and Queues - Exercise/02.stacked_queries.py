lines = int(input())
stack = []

for i in range(lines):
    action = input().split()
    if len(action) > 1:
        stack.append(int(action[1]))
    elif stack:
        if action[0] == "2":
            stack.pop()
        elif action[0] == "3":
            print(max(stack))
        elif action[0] == "4":
            print(min(stack))

stack.reverse()
print(", ".join(map(str, stack)))
