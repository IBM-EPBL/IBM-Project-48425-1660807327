from flask import Flask, render_template, request, redirect, session 
import ibm_db
import re

app = Flask(__name__)


app.secret_key = 'a'
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=;PWD=;",'','')
#HOME--PAGE
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' :
        name = request.form['name']
        profession = request.form['profession']
        email = request.form['email']
        password = request.form['password']
        confirm_password= request.form['confirm_password']
        

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM register WHERE name = % s', (name ))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute('INSERT INTO register VALUES ( % s, % s, % s,% s,% s)', (username, profession,email,password,confirm_password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            return render_template('signup.html', msg = msg)
        
        
 
        
 #LOGIN--PAGE
    
@app.route("/signin")
def signin():
    return render_template("login.html")
        
@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        name = request.form['name']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM register WHERE username = % s AND password = % s', (username, password ),)
        account = cursor.fetchone()
        print (account)
        
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid=  account[0]
            session['username'] = account[1]
           
            return redirect('/home')
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

#ADDING----DATA


@app.route("/add")
def adding():
    return render_template('add_expense.html')


@app.route('/addexpense',methods=['GET', 'POST'])
def addexpense():
    type = request.form['type']
    date = request.form['date']
    name = request.form['ename']
    amount = request.form['amount']
    
    
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO expenses VALUES ( % s, % s, % s, % s, % s)', (session['id'] , type, date, name, amount))
    mysql.connection.commit()
    print(date + " " + name + " " + amount + " " + type)
    
    return redirect("/display")





#DISPLAY---graph 

@app.route("/display")
def display():
    print(session["username"],session['id'])
   
       
    return render_template('chart.html' ,expense = expense)
    return render_template('chart1.html' ,expense = expense)
                          
                          




 #limit
@app.route("/limit" )
def limit():
       return redirect('/limitn')

@app.route("/limitnum" , methods = ['POST' ])
def limitnum():
     if request.method == "POST":
         number= request.form['number']
         cursor = mysql.connection.cursor()
         cursor.execute('INSERT INTO limits VALUES (% s, % s) ',(session['id'], number))
         mysql.connection.commit()
         return redirect('/limitn')
            

if __name__ == "__main__":
    app.run(debug=True)
