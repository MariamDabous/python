from unicodedata import name
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template("index.html")


@app.route('/result',methods=['POST'])
def index1():
    name=request.form['name']
    location=request.form['location']
    language=request.form['language']
    comment=request.form['comment']
    return render_template("index2.html",info1=name,info2=location,info3=language,info4=comment)


if __name__=="__main__":
    app.run(debug=True) 