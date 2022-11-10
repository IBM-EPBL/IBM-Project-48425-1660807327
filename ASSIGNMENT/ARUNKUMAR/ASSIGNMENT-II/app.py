from flask import Flask,request,render_template
import flask

app= Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/form_login',methods=['POST','GET'])
def login():
    email=request.form['email']
    pwd=request.form['password']

    if email1 not in database:
        return render_template('login.html')
        else:
    if database[email1]!=pwd:
       return render_template('login.html',info='invalid password')
        else:
        return_template('login.html',email=email1)

    if __name__ =='__main__':
        app.run()