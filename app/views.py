from flask import render_template
from app import app

@app.route('/')
  def index():
      return render_template("login.html")

@app.route('/home')
  def view():
      return render_template("home.html")

@app.route('/signup')
  def signup():
      return render_template("signup")



@app.route('/view')   
  def view():
      return render_template("/view")                