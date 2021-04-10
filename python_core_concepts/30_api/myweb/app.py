from flask import Flask

app = Flask("myiiec")

@app.route('/form')
def myform():
  return "form"

@app.route('/data')
def mydata():
  return "data"

app.run(port=5555, debug=True)
