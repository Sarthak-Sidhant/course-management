from flask import Flask, render_template, request

app = Flask(__name__)

# define a function to read the courses from the file
def read_courses():
    courses = []
    with open("courses.txt", "r") as file:
        for line in file:
            course_data = line.strip().split(",")
            course = {
                "name": course_data[0],
                "branch": course_data[1],
                "state": course_data[2],
                "college": course_data[3],
                "university": course_data[4],
                "price": course_data[5]
            }
            courses.append(course)
    return courses

@app.route("/")
def home():
    courses = read_courses()
    return render_template("home.html", courses=courses)

@app.route('/results', methods=['GET', 'POST'])
def results():
    name = request.form['name']
    branch = request.form['branch']
    state = request.form['state']
#what
    filtered_courses = []

    with open('courses.txt', 'r') as f:
        for line in f:
            course, course_branch, course_state, college, university, price = line.strip().split(',')
            if (not name or name == course) and (not branch or branch == course_branch) and (not state or state == course_state):
                filtered_courses.append((course, course_branch, course_state, college, university, price))

    return render_template('results.html', courses=filtered_courses)

if __name__ == "__main__":
    app.run(debug=True)
