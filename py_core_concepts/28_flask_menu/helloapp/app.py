from flask import Flask, render_template, request

app = Flask("myapp")

@app.route("/")
def home():
     return("home page")

@app.route("/menu", methods=["GET"])
def mymenu():
    name = request.args.get("name")
    cname = request.args.get("cname")
    htmlcode = render_template("mymenu.html", name=name, cname=cname)
    return htmlcode

@app.route("/form")
def myform():
    return render_template("form.html")
