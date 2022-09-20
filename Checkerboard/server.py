from turtle import color, width
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    x=8
    y=8
    return render_template("index3.html", width=int(x), height=int(y))

@app.route('/4')
def index2():
    x=8
    y=4
    return render_template("index3.html", width=int(x), height=int(y))

@app.route('/<x>/<y>')
def index3(x,y):
    return render_template("index3.html", width=int(x), height=int(y))

@app.route('/<x>/<y>/<color1>/<color2>')
def index4(x,y,color1,color2):
    return render_template("index3.html", width=int(x), height=int(y),c1=color1,c2=color2)

if __name__=="__main__":
    app.run(debug=True)
