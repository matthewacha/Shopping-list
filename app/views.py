from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
  return render_template("Login.html")

@app.route('/home')
def view():
  return render_template("Home.html")

@app.route('/signup')
def signup():
  return render_template("Signup")



@app.route('/view_items')   
def view():
  return render_template("/view")                