import datetime

from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    now=datetime.datetime.now()
    DIWALI=now.month==10 and now.day==26
    return render_template("index.html",DIWALI=DIWALI)
