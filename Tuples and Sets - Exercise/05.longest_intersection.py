n = int(input())
max_len = 0
longest_intersection = ''

for i in range(n):
    first_range, second_range = input().split('-')

    first_range = list(map(int, first_range.split(',')))
    second_range = list(map(int, second_range.split(',')))

    intersect_start = max(first_range[0], second_range[0])
    intersect_end = min(first_range[1], second_range[1])

    intersection = list(range(intersect_start, intersect_end + 1))

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
        max_len = len(longest_intersection)

print(f"Longest intersection is {longest_intersection} with length {max_len}")
