from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "Secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['your_name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(request.form['your_name']) < 1:
        flash("Name cannot be empty")
    else:
        flash("success")

    if len(request.form['comment']) < 1:
        flash("Comment cannot be empty")
    elif len(request.form['comment']) > 120:
        flash("comment cannot be more than 120 characters")
    else:
        flash("success")
    
        

    return render_template('/result.html', name=request.form['your_name'], location=request.form['location'],language=request.form['language'],comment=request.form['comment'])
    return redirect ("/")

app.run(debug=True)