def best_list_pureness(*args):
    numbers, num = args[0], args[1]

    best_pureness, rotations, rotation_sum = 0, 0, 0

    for i in range(num):

        for el in numbers:
            rotation_sum += numbers.index(el) * el

        if rotation_sum > best_pureness:
            best_pureness = rotation_sum
            rotations = i

        rest_nums = numbers[:-1]
        numbers = [numbers[-1]]
        numbers.extend(rest_nums)

        rotation_sum = 0

    return f"Best pureness {best_pureness} after {rotations} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
