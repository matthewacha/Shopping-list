from flask import flask
app=Flask(__name__,instance_relative_config=True)

from app import views

app.config.from object('config')