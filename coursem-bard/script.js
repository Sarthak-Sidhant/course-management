function filterCourses(courses, criteria) {
    filteredCourses = [];
    for (const course of courses) {
        if (criteria in course) {
            filteredCourses.push(course);
        }
    }
    return filteredCourses;
}

function displayCourses(courses) {
    for (const course of courses) {
        console.log(course);
    }
}

const criteria = prompt("Enter the criteria to filter the courses: ");
const filteredCourses = filterCourses(courses, criteria);
displayCourses(filteredCourses);
