number_students = int(input())
student_grades = {}

for _ in range(number_students):
    name, grade_as_str = tuple(input().split())
    grade = float(grade_as_str)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for k, v in student_grades.items():
    avg = (sum(v) / len(v))
    formatted_grades = f"{' '.join([f'{g:.2f}' for g in v])}"
    print(f"{k} ->", formatted_grades, f"(avg: {avg:.2f})")
