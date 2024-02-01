def students_credits(*info):
    courses = {}
    total_credits = 0
    result = ""

    for data in info:
        course_name, course_credits, max_points, diyans_points = data.split("-")
        took_percentage = int(diyans_points) / int(max_points)
        points = int(course_credits) * took_percentage

        total_credits += points
        courses[course_name] = points

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    for course, points in sorted(courses.items(), key=lambda x: -x[1]):
        result += f"{course} - {float(points):.1f}\n"

    return result


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

