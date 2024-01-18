from collections import deque

substrings = deque(input().split())
mid_index = len(substrings) // 2
main_colors = "red", "yellow", "blue"
secondary_colors = "orange", "purple", "green"

left_string = substrings.popleft()
right_string = substrings.pop()

string = left_string + right_string

if string not in main_colors and string not in secondary_colors:
    left_part = substrings[:mid_index]
    right_part = substrings[mid_index:]
    substrings = deque()
    substrings.append(left_part)
    substrings.append(string)
    substrings.append(right_part)

print(substrings)
