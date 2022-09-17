from ast import Num
from turtle import color
from flask import Flask , render_template
app = Flask(__name__)    


@app.route('/')          
def hello_world():
    return ('helllo') 

@app.route('/play')          
def level1():
    return render_template ('index.html')

@app.route('/play/<x>')          
def level2(x):
    return render_template('index2.html', boxes=int(x))

@app.route('/play/<x>/<color>')          
def level3(x,color):
    return render_template('index3.html', boxes=int(x), box_color=color)





if __name__=="__main__":   
    app.run(debug=True)    

