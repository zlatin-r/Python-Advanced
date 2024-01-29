def softuni_students(*args, **kwargs):
    students = {}
    invalid_students = []
    result = ""

    for id, name in args:

        if id in kwargs.keys():
            students[name] = []
            students[name].append(kwargs[id])
        else:
            invalid_students.append(name)

    students = sorted(students.items(), key=lambda x: x[0])

    for k, v in students:
        result += f"*** A student with the username {k} has successfully finished the course {''.join(v)}!\n"
    if invalid_students:
        result += f"!!! Invalid course students: " + ", ".join(sorted(invalid_students))

    return result


print(softuni_students(
    ('id_1', 'John'),
    ('id_3', 'Bob'),
    ('id_4', 'Eve'),
    ('id_2', 'Alice'),
    ('id_43', 'Chris'),
    ('id_12', 'Mariya'),
    id_1='Course 1',
    id_3='Course 2',
    id_12='Course 3',
))

