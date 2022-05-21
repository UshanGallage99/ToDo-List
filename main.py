from curses import flash
from distutils.log import debug
import imp


from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/task")
def task():
    logged_user=session["username"]  
    return render_template("task.html",username=logged_user)

@app.route("/logout",methods=["POST"])
def logout():

    if request.method=="POST":
        session["username"]=None
        return redirect("/")
     
@app.route("/login", methods=["POST","GET"])
def login():

    if request.method=="POST":
        session["username"]=request.form["username"]
        return redirect("/task") 
    return render_template("login.html")
    
if __name__=="__main__":
    app.run(debug=True)