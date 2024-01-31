from collections import deque

tasks_time = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

ducks = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while tasks_time and number_of_tasks:

    curr_task_time = tasks_time.popleft()
    curr_num_tasks = number_of_tasks.pop()

    time_needed = curr_task_time * curr_num_tasks

    if time_needed <= 60:
        ducks["Darth Vader Ducky"] += 1
    elif 61 <= time_needed <= 120:
        ducks["Thor Ducky"] += 1
    elif 121 <= time_needed <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
    elif 181 <= time_needed <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        curr_num_tasks -= 2
        number_of_tasks.append(curr_num_tasks)
        tasks_time.append(curr_task_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for ducky, count in ducks.items():
    print(f"{ducky}: {count}")
