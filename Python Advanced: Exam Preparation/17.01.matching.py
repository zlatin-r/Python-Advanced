from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches = 0

while females and males:

    curr_female = females.popleft()
    curr_male = males.pop()

    if curr_female <= 0:
        males.append(curr_male)
        continue

    if curr_female % 25 == 0:
        males.append(curr_male)
        females.popleft()
        continue

    if curr_male <= 0:
        females.appendleft(curr_female)
        continue

    if curr_male % 25 == 0:
        females.appendleft(curr_female)
        males.pop()
        continue

    if curr_female != curr_male:
        curr_male -= 2
        males.append(curr_male)
    else:
        matches += 1

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
