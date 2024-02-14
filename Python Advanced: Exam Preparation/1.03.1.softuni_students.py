def softuni_students(*args, **kwargs):
    users_data = []
    invalid_students = []
    result = ""

    for course_id, username in args:
        if course_id in kwargs.keys():
            users_data.append(f"*** A student with the username {username} has successfully finished the course {kwargs[course_id]}!")
        else:
            invalid_students.append(username)

    for student in sorted(users_data):
        result += f"{student}\n"

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return result


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
