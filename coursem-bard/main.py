import json

with open("database.json") as f:
    courses = json.load(f)

def filter_courses(courses, criteria):
    filtered_courses = []
    for course in courses:
        if criteria in course:
            filtered_courses.append(course)
    return filtered_courses

if __name__ == "__main__":
    criteria = input("Enter the criteria to filter the courses: ")
    filtered_courses = filter_courses(courses, criteria)
    print("The filtered courses are:")
    for course in filtered_courses:
        print(course)
