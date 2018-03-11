from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsASecret"


# Index page.
@app.route('/')
def index(): 
    if 'number' not in session.keys():
        session['state'] = 'new'
        session['number'] = random.randrange(1, 101)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['number']) == int(session['number']):
        session['state'] = 'win'
    elif int(request.form['number']) < int(session['number']):
        session['state'] = 'low'
    elif int(request.form['number']) > int(session['number']):
        session['state'] = 'high'

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.pop('number')
    return redirect('/')

app.run(debug=True)
