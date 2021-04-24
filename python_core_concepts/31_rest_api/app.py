from flask import Flask, request, render_template, jsonify

app = Flask("myiiec")

db = [
    {
        # first student
        "id": 1,
        "name": "rasul",
        "contact": [
            {
                "name": "mob",
                "number": 11111
            },
            {
                "name": "lambline",
                "number": 2222
            }
        ]

    },
    {
        # second student
        "id": 2,
        "name": "john",
        "surname": "doel"
    }
]

@app.route('/spost', methods=["GET"])
def f1():
    return jsonify(db)

@app.route('/spost', methods=["DELETE"])
def f2():
    return "delete a post"

@app.route('/spost', methods=["PUT"])
def f3():
    return "update a post"

@app.route('/spost', methods=["POST"])
def f4():
    return "create a post"

app.run(port=5555, debug=True)