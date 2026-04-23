from flask import Flask, render_template, request
import random

app = Flask(__name__)

number = random.randint(1, 100)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    global number
    message = ""
    if request.method == 'POST':
        user = int(request.form['num'])
        if user == number:
            message = "🎉 Correct!"
            number = random.randint(1, 100)
        elif user > number:
            message = "Too High"
        else:
            message = "Too Low"
    return render_template('guess.html', msg=message)

@app.route('/tic')
def tic():
    return render_template('tic.html')

if __name__ == '__main__':
    app.run(debug=True)
