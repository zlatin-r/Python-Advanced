def numbers_searching(*nums):
    numbers, min_num, max_num = list(nums), min(nums), max(nums)

    missing_nums = []
    repeated_nums = []

    for i in range(min_num, max_num + 1):

        if i not in numbers:
            missing_nums.append(i)

        if numbers.count(i) > 1:
            repeated_nums.append(i)

    missing_nums.append(repeated_nums)

    return missing_nums


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
