def gather_credits(credits_needed, *args):
    enrolled = []
    collected_credits = 0

    for arg in args:
        if arg[0] not in enrolled and credits_needed > collected_credits:
            collected_credits += int(arg[1])
            enrolled.append(arg[0])

    if collected_credits >= credits_needed:
        return f"Enrollment finished! Maximum credits: {collected_credits}.\nCourses: {', '.join(sorted(enrolled))}"
    else:
        return f"You need to enroll in more courses! You have to gather {credits_needed - collected_credits} credits more."


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
