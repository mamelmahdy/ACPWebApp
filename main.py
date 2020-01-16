from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from questions import questions
import ast

app = Flask(__name__)

bs = Bootstrap(app)

user = {'firstName': '', 'lastName': '', 'userName': ''}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def loginUser():
    user['firstName'] = 'Jane'
    user['lastName'] = 'Doe'
    user['userName'] = request.form['user']
    print("User %s logged in with password %s" % (request.form['user'], request.form['password']))
    return redirect('/home')

@app.route('/profile')
def profile():
    return render_template('profile.html', user=user)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/question/<int:questionID>', methods=['GET','POST'])
def question(questionID):
    if request.method == 'GET':
        return render_template('question.html', question=questions[questionID])
    if request.method == 'POST':
        response = ast.literal_eval(request.form[str(questionID)])
        print("Question %d answer leads to %s %d" % (questionID, response[0], response[1]))
        if  response[0] == 'question':
            return redirect('/question/' + str(response[1]))
        else:
            return redirect('/video/' + str(response[1]))

@app.route('/video/<int:videoID>', methods=['GET','POST'])
def video(videoID):
    if request.method == 'GET':
        return render_template('video.html', video={'id':'1'})
    if request.method == 'POST':
        return redirect('/question/0')

if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
