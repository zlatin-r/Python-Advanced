numbers = tuple(float(x) for x in input().split())

same_nums = {}

for number in numbers:
    if number not in same_nums:
        same_nums[number] = numbers.count(number)

for k, v in same_nums.items():
    print(f"{k} - {v} times")
