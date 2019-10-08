from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    if request.method == 'GET':
        return "Please Input A Number."
    else:
        userData = dict(request.form)
        userNum = userData['userNum']
    return render_template("index.html", userNum = userNum)
