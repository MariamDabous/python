from flask import Flask, render_template,redirect,request, session
app = Flask(__name__)
app.secret_key='ggggggggggggggggggg'


@app.route('/')          
def counter():
    if 'visits' not in session:
        session['visits']=0
    else:
        session['visits']+=1
    
    return render_template('index.html', num=session['visits'])  

@app.route('/destroy_session')          
def destroy():
    session.clear()

    return render_template('index.html') 


if __name__=="__main__":   
    app.run(debug=True)    
