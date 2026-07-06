from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

from commands import execute_command

@app.route("/command", methods=["POST"])
def command():

    data = request.json

    response = execute_command(data["text"])
    text = data["text"].lower()
    
     

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)