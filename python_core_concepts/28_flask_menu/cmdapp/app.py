from flask import Flask
from flask import render_template
from flask import request
import subprocess

app = Flask("cmdmenu")

@app.route("/form")
def myform():
    data = render_template("myform.html")
    return data

@app.route("/cmd", methods=["GET"])
def mycmd():
    cmd = request.args.get("cmd")
    data = subprocess.getoutput(cmd)
    return "<pre>" + data + "</pre>"
