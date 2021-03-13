from flask import Flask, render_template
import subprocess

app = Flask("myapp")


@app.route("/hello")
def myhello():
  return("<b>hi</b>")

@app.route("/date")
def mysearch():
  print("my server date")
  data = subprocess.getoutput("date")
  return(data)

@app.route("/email")
def myemail():
  return render_template("email.html")


