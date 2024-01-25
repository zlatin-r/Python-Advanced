def age_assignment(*args, **kwargs):
    data = {}
    result = ""

    for arg in args:
        if arg[0] in kwargs.keys():
            data[arg] = kwargs[arg[0]]

    sorted_data = sorted(data.items())

    for key, value in sorted_data:
        result += f"{key} is {value} years old.\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
