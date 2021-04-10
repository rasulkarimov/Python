from flask import Flask, request, render_template

app = Flask("myiiec")

# get form
@app.route('/form_get')
def myform_get():
  return render_template("basic_get.html")

# post form 
@app.route('/form_post')
def myform():
  return render_template("basic_post.html")

# dynamic route
@app.route('/name/<y>')
def myname(y):
  return y

@app.route('/data', methods=['POST', 'GET'])
def mydata():
  if request.method == 'POST':
    data = request.form.get('x')
    print(data)
  elif request.method == 'GET':
    data = request.args.get('x')
    print(data)
  return data

app.run(port=5555, debug=True)
