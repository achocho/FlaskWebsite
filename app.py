from flask import Flask, render_template,request,Response,url_for,redirect
import sqlite3
import os
currentdirectory=os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder='templateFiles', static_folder='assets')



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/register',methods={"POST"})
def register1():
    username=request.form["username"]
    password=request.form["pass"]
    connection= sqlite3.connect(currentdirectory + "/users.db")
    cursor=connection.cursor()
    query1="INSERT INTO users VALUES('{usn}','{psw}')".format(usn=username,psw=password)
    cursor.execute(query1)
    connection.commit()
    return render_template("register.html")

@app.route('/login',methods={"POST"})
def login1():
    try:
        if request.method=="POST":
            name=request.form.get("username")
            password=request.form.get("pass")
            connection=sqlite3.connect(currentdirectory+"/users.db")
            cursor=connection.cursor()
            query1 = "SELECT * FROM users WHERE username = ? AND password = ?"
            result=cursor.execute(query1,(name,password))
            result=result.fetchall()[0][0]
            resp=redirect(url_for("index"))
            resp.set_cookie("Logged","+",max_age=3600)
            return resp
    except:
        return render_template("login.html",test="Something happened. Username or password is/are incorrect!")





if __name__ == '__main__':
    app.run(debug=True)