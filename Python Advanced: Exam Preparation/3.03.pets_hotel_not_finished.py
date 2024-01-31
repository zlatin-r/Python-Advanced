def accommodate_new_pets(capacity, max_weight, *animal_data):
    accommodated_pets = {}
    passed_animals = []

    for animal_type, weight in animal_data:
        if weight <= max_weight and capacity > 0:
            passed_animals.append(animal_type)
            capacity -= 1

    for animal in passed_animals:
        if animal not in accommodated_pets:
            accommodated_pets[animal] = 0
        accommodated_pets[animal] += 1

    if len(passed_animals) == sum(accommodated_pets.values()):
        result = f"All pets are accommodated! Available capacity: {capacity}.\n"
    else:
        result = "You did not manage to accommodate all pets!\n"
    result += "Accommodated pets:\n"

    for k, v in sorted(accommodated_pets.items()):
        result += f"{k}: {v}\n"

    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
