from flask import Flask  
app = Flask(__name__)  
@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')          
def dojo():
    return 'dojo'
#-------------------3
@app.route('/say/<name>')          
def say(name):
    return "Hi "+name

@app.route('/repeat/<intager>/<name>')          
def int_to(name,intager):
    str= ""
    for i in range(0,int(intager)):
        str=str+ name + "<br>"
    return str



if __name__=="__main__":  
    app.run(debug=True)    
