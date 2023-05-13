from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    return render_template('results.html', name=name, age=age, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)
#run