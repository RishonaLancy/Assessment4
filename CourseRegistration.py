courses = {
    "DBMS": {
        "credits": 4,
        "prerequisite": "Programming",
        "time": "10:00"
    },
    "AI": {
        "credits": 4,
        "prerequisite": "Data Structures",
        "time": "11:00"
    },
    "ML": {
        "credits": 3,
        "prerequisite": "Statistics",
        "time": "10:00"
    },
    "Cloud": {
        "credits": 3,
        "prerequisite": "Networking",
        "time": "12:00"
    }
}

student_id = "S101"
semester = 5
credit_limit = 12

completed_courses = [
    "Programming",
    "Data Structures",
    "Statistics",
    "Networking"
]

selected_courses = ["DBMS", "AI", "ML"]

registered_courses = []


def register_course(course):

    if course not in courses:
        print(course, "- Invalid course")
        return

    if course in registered_courses:
        print(course, "- Duplicate registration")
        return

    details = courses[course]

    if details["prerequisite"] not in completed_courses:
        print(course, "- Missing prerequisite")
        return

    current_credits = sum(
        courses[c]["credits"] for c in registered_courses
    )

    if current_credits + details["credits"] > credit_limit:
        print(course, "- Credit limit exceeded")
        return

    for registered in registered_courses:
        if courses[registered]["time"] == details["time"]:
            print(course, "- Timetable conflict")
            return

    registered_courses.append(course)
    print(course, "- Registration successful")


print("Student ID:", student_id)
print("Semester:", semester)
print("Credit Limit:", credit_limit)
print()

for course in selected_courses:
    register_course(course)

print("\nRegistered Courses:")

total_credits = 0

for course in registered_courses:
    print(course, "-", courses[course]["credits"], "credits")
    total_credits += courses[course]["credits"]

print("Total Registered Credits:", total_credits)
